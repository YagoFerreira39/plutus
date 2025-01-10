from abc import ABC, abstractmethod

from src.domain.models.billing_data_model import BillingDataModel


class IBillingDataRepository(ABC):
    @classmethod
    @abstractmethod
    async def register_billing_data_batch(
        cls, billing_data_model_list: list[BillingDataModel]
    ) -> None:
        pass

    @classmethod
    @abstractmethod
    async def get_billing_data_by_debt_ids(cls, debt_ids: list[str]) -> list[BillingDataModel]:
        pass

    @classmethod
    @abstractmethod
    async def get_billing_data_by_status(cls, status: str) -> list[BillingDataModel]:
        pass

    @classmethod
    @abstractmethod
    async def update_billing_data_status(
        cls, billing_data_model: BillingDataModel
    ) -> None:
        pass
