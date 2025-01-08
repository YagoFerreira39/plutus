import loglifos

from src.adapters.repositories.exceptions.repository_base_exception import (
    RepositoryBaseException,
)

from src.domain.models.billing_data_model import BillingDataModel
from src.use_cases.exceptions.use_case_exceptions import (
    UnexpectedUseCaseException,
    UnableToSendBillingDataEmailException,
)

from src.use_cases.exceptions.use_case_base_exception import UseCaseBaseException
from witch_doctor import WitchDoctor

from src.use_cases.ports.extensions.process_billing.i_process_billing_data_extension import (
    IProcessBillingDataExtension,
)
from src.use_cases.ports.repositories.mongo_db.i_billing_data_repository import (
    IBillingDataRepository,
)
from src.use_cases.ports.services.i_email__service import IEmailService
from src.use_cases.ports.use_cases.i_send_billing_email_use_case import (
    ISendBillingEmailUseCase,
)


class SendBillingEmailUseCase(ISendBillingEmailUseCase):
    __process_billing_data_extension: IProcessBillingDataExtension
    __billing_data_repository: IBillingDataRepository
    __email_service: IEmailService

    @WitchDoctor.injection
    def __init__(
        self,
        process_billing_data_extension: IProcessBillingDataExtension,
        billing_data_repository: IBillingDataRepository,
        email_service: IEmailService,
    ):
        SendBillingEmailUseCase.__process_billing_data_extension = (
            process_billing_data_extension
        )
        SendBillingEmailUseCase.__billing_data_repository = billing_data_repository
        SendBillingEmailUseCase.__email_service = email_service

    @classmethod
    async def send_pending_billings(cls) -> None:
        try:
            billing_data_with_pending_status = (
                await cls.__get_billing_data_with_pending_status()
            )

            await cls.__send_pending_billing_via_email(
                model_list=billing_data_with_pending_status
            )

        except UseCaseBaseException as original_exception:
            raise original_exception

        except Exception as original_exception:
            raise UnexpectedUseCaseException(
                message="An unexpected error occurred.",
                original_error=original_exception,
            ) from original_exception

    @classmethod
    async def __get_billing_data_with_pending_status(cls) -> list[BillingDataModel]:
        try:
            model_list = await cls.__billing_data_repository.get_billing_data_by_status(
                status="pending"
            )

            return model_list

        except RepositoryBaseException as original_exception:
            loglifos.error(msg=f"Unable to send billing data email.")

            raise UnableToSendBillingDataEmailException(
                message="Unable to send billing data email.",
                original_error=original_exception,
            ) from original_exception

    @classmethod
    async def __send_pending_billing_via_email(
        cls, model_list: list[BillingDataModel]
    ) -> None:
        try:
            for model in model_list:
                await cls.__email_service.send_email(model=model)

                await cls.__update_billing_data_status_batch(model=model)

        except RepositoryBaseException as original_exception:
            loglifos.error(msg=f"Unable to send billing data email.")

            raise UnableToSendBillingDataEmailException(
                message="Unable to send billing data email.",
                original_error=original_exception,
            ) from original_exception

    @classmethod
    async def __update_billing_data_status_batch(cls, model: BillingDataModel) -> None:
        try:
            await cls.__billing_data_repository.update_billing_data_status(
                billing_data_model=model
            )

            loglifos.info(
                msg=f"Billing sent via email with status updated - {model.billing_id}"
            )

        except RepositoryBaseException as original_exception:
            loglifos.error(msg=f"Unable to send billing data email.")

            raise UnableToSendBillingDataEmailException(
                message="Unable to send billing data email.",
                original_error=original_exception,
            ) from original_exception
