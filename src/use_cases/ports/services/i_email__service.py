from abc import ABC, abstractmethod

from src.domain.models.billing_data_model import BillingDataModel


class IEmailService(ABC):

    @classmethod
    @abstractmethod
    async def send_email(cls, model: BillingDataModel) -> None:
        pass
