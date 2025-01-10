from abc import ABC, abstractmethod

from fastapi import UploadFile

from src.domain.entities.billing_data_entity import BillingDataEntity
from src.domain.entities.billing_file_entity import BillingFileEntity
from src.domain.models.billing_data_model import BillingDataModel
from src.use_cases.data_types.dtos.process_billing.process_billing_data_dto import (
    ProcessBillingDataDto,
)
from src.use_cases.data_types.requests.process_billing.process_billing_data_request import (
    ProcessBillingDataRequest,
)
from src.use_cases.data_types.responses.process_billing_data_response import (
    ProcessBillingDataResponse,
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
        file: UploadFile,
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

    @staticmethod
    @abstractmethod
    def from_model_list_to_dto(
        model_list: list[BillingDataModel],
    ) -> ProcessBillingDataDto:
        pass

    @staticmethod
    @abstractmethod
    def from_dto_to_response(dto: ProcessBillingDataDto) -> ProcessBillingDataResponse:
        pass
