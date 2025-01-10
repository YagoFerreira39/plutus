from abc import ABC, abstractmethod

from src.use_cases.data_types.dtos.process_billing.process_billing_data_dto import (
    ProcessBillingDataDto,
)
from src.use_cases.data_types.requests.process_billing.process_billing_data_request import (
    ProcessBillingDataRequest,
)


class IProcessBillingDataUseCase(ABC):

    @classmethod
    @abstractmethod
    async def execute(cls, request: ProcessBillingDataRequest) -> ProcessBillingDataDto:
        pass
