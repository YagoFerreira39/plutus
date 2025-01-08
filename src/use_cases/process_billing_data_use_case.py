from src.adapters.repositories.exceptions.repository_base_exception import (
    RepositoryBaseException,
)

from src.domain.exceptions.entity_base_exception import EntityBaseException

from src.adapters.extensions.exceptions.extension_base_exception import (
    ExtensionBaseException,
)

from src.domain.entities.billing_file_entity import BillingFileEntity
from src.domain.models.billing_data_model import BillingDataModel
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
    async def execute(cls, request: ProcessBillingDataRequest) -> None:
        try:
            billing_file_entity = await cls.__create_billing_file_entity(
                request=request
            )

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
            entity = await cls.__create_billing_file_entity(request=request)

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
    async def __get_billing_data(
        cls, billing_data_model: BillingDataModel
    ) -> BillingDataModel:
        try:
            billing_data_model = (
                await cls.__billing_data_repository.get_billing_data_by_id(
                    billing_id=billing_data_model.billing_id
                )
            )

            return billing_data_model

        except RepositoryBaseException as original_exception:
            raise UnableToProcessBillingDataException(
                message="unable to process billing data.",
                original_error=original_exception.original_error,
            ) from original_exception
