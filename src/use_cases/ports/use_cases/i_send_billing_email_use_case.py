from abc import ABC, abstractmethod


class ISendBillingEmailUseCase(ABC):

    @classmethod
    @abstractmethod
    async def send_pending_billings(cls) -> None:
        pass
