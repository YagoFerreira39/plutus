import loglifos

from src.domain.models.billing_data_model import BillingDataModel
from src.externals.services.exceptions.service_exceptions import (
    FailToSendEmailException,
)
from src.use_cases.ports.services.i_email__service import IEmailService


class EmailService(IEmailService):

    @classmethod
    async def send_email(cls, model: BillingDataModel) -> None:
        try:
            loglifos.info(msg=f"Simulating sending email to {model.email}.")

        except Exception as original_exception:
            raise FailToSendEmailException(
                message="Fail to send email.",
                original_error=original_exception,
            ) from original_exception
