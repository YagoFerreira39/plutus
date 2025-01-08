from abc import ABC, abstractmethod

from src.domain.entities.billing_data_entity import BillingDataEntity
from src.domain.entities.billing_file_entity import BillingFileEntity
from src.domain.models.billing_data_model import BillingDataModel
from src.use_cases.data_types.requests.process_billing.process_billing_data_request import (
    ProcessBillingDataRequest,
)
from src.use_cases.data_types.router_requests.process_billing.process_billing_data_router_request import (
    ProcessBillingDataRouterRequest,
)


class IProcessBillingDataExtension(ABC):

    @staticmethod
    @abstractmethod
    def from_result_to_model(result: dict) -> BillingDataModel:
        pass

    @staticmethod
    @abstractmethod
    def from_result_list_to_model_list(
        result_list: list[dict],
    ) -> list[BillingDataModel]:
        pass

    @staticmethod
    @abstractmethod
    def from_router_request_to_request(
        router_request: ProcessBillingDataRouterRequest,
    ) -> ProcessBillingDataRequest:
        pass

    @staticmethod
    @abstractmethod
    async def from_request_to_entity(
        request: ProcessBillingDataRequest,
    ) -> BillingFileEntity:
        pass

    @staticmethod
    @abstractmethod
    def from_entity_list_to_model_list(
        entity_list: list[BillingDataEntity],
    ) -> list[BillingDataModel]:
        pass
