from src.adapters.repositories.exceptions.repository_base_exception import (
    RepositoryBaseException,
)
from src.domain.entities.billing_data_entity import BillingDataEntity

from src.domain.exceptions.entity_base_exception import EntityBaseException

from src.adapters.extensions.exceptions.extension_base_exception import (
    ExtensionBaseException,
)

from src.domain.entities.billing_file_entity import BillingFileEntity
from src.domain.models.billing_data_model import BillingDataModel
from src.use_cases.data_types.dtos.process_billing.process_billing_data_dto import (
    ProcessBillingDataDto,
)
from src.use_cases.exceptions.use_case_exceptions import (
    UnexpectedUseCaseException,
    MalformedRequestInputException,
    UnableToProcessBillingDataException,
)

from src.use_cases.exceptions.use_case_base_exception import UseCaseBaseException
from witch_doctor import WitchDoctor

from src.use_cases.data_types.requests.process_billing.process_billing_data_request import (
    ProcessBillingDataRequest,
)
from src.use_cases.ports.extensions.process_billing.i_process_billing_data_extension import (
    IProcessBillingDataExtension,
)
from src.use_cases.ports.repositories.mongo_db.i_billing_data_repository import (
    IBillingDataRepository,
)
from src.use_cases.ports.use_cases.i_process_billing_data_use_case import (
    IProcessBillingDataUseCase,
)


class ProcessBillingDataUseCase(IProcessBillingDataUseCase):
    __process_billing_data_extension: IProcessBillingDataExtension
    __billing_data_repository: IBillingDataRepository

    @WitchDoctor.injection
    def __init__(
        self,
        process_billing_data_extension: IProcessBillingDataExtension,
        billing_data_repository: IBillingDataRepository,
    ):
        ProcessBillingDataUseCase.__process_billing_data_extension = (
            process_billing_data_extension
        )
        ProcessBillingDataUseCase.__billing_data_repository = billing_data_repository

    @classmethod
    async def execute(cls, request: ProcessBillingDataRequest) -> ProcessBillingDataDto:
        try:
            billing_file_entity = await cls.__create_billing_file_entity(
                request=request
            )

            billing_data_model_list = await cls.__create_billing_data_model_list(
                billing_data_entity_list=billing_file_entity.data
            )

            await cls.__register_billing_data_batch(
                billing_data_model_list=billing_data_model_list
            )

            dto = cls.__create_dto(billing_data_model_list=billing_data_model_list)

            return dto

        except UseCaseBaseException as original_exception:
            raise original_exception

        except Exception as original_exception:
            raise UnexpectedUseCaseException(
                message="An unexpected error occurred.",
                original_error=original_exception,
            ) from original_exception

    @classmethod
    async def __create_billing_file_entity(
        cls, request: ProcessBillingDataRequest
    ) -> BillingFileEntity:
        try:
            entity = await cls.__process_billing_data_extension.from_request_to_entity(
                request=request
            )

            return entity

        except EntityBaseException as original_exception:
            raise MalformedRequestInputException(
                message=original_exception.message,
                original_error=original_exception.original_error,
            ) from original_exception
        except ExtensionBaseException as original_exception:
            raise UnableToProcessBillingDataException(
                message="unable to process billing data.",
                original_error=original_exception.original_error,
            ) from original_exception

    @classmethod
    async def __create_billing_data_model_list(
        cls, billing_data_entity_list: list[BillingDataEntity]
    ) -> list[BillingDataModel]:
        try:
            model_list = (
                cls.__process_billing_data_extension.from_entity_list_to_model_list(
                    entity_list=billing_data_entity_list
                )
            )

            new_model_list = await cls.__exclude_billing_data_already_processed(
                model_list=model_list
            )

            return new_model_list
        except ExtensionBaseException as original_exception:
            raise UnableToProcessBillingDataException(
                message="unable to process billing data.",
                original_error=original_exception.original_error,
            ) from original_exception

    @classmethod
    async def __exclude_billing_data_already_processed(
        cls, model_list: list[BillingDataModel]
    ) -> list[BillingDataModel]:
        try:
            billing_data_debt_ids = [model.debt_id for model in model_list]

            billing_data_model_list_from_database = (
                await cls.__billing_data_repository.get_billing_data_by_debt_ids(
                    debt_ids=billing_data_debt_ids
                )
            )
            billing_data_debt_ids_from_database = [
                model.debt_id for model in billing_data_model_list_from_database
            ]

            new_billing_data_model_list = [
                model
                for model in model_list
                if not model.debt_id in billing_data_debt_ids_from_database
            ]

            return new_billing_data_model_list

        except RepositoryBaseException as original_exception:
            raise UnableToProcessBillingDataException(
                message="unable to process billing data.",
                original_error=original_exception.original_error,
            ) from original_exception

    @classmethod
    async def __register_billing_data_batch(
        cls, billing_data_model_list: list[BillingDataModel]
    ) -> None:
        try:
            await cls.__billing_data_repository.register_billing_data_batch(
                billing_data_model_list=billing_data_model_list
            )

        except RepositoryBaseException as original_exception:
            raise UnableToProcessBillingDataException(
                message="unable to process billing data.",
                original_error=original_exception.original_error,
            ) from original_exception

    @classmethod
    def __create_dto(
        cls, billing_data_model_list: list[BillingDataModel]
    ) -> ProcessBillingDataDto:
        try:
            dto = cls.__process_billing_data_extension.from_model_list_to_dto(
                model_list=billing_data_model_list
            )

            return dto

        except ExtensionBaseException as original_exception:
            raise UnableToProcessBillingDataException(
                message="unable to process billing data.",
                original_error=original_exception.original_error,
            ) from original_exception
