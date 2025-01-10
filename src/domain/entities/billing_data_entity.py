import datetime
from dataclasses import dataclass

from src.domain.entities.value_objects.date_entity import DateEntity
from src.domain.entities.value_objects.id_entity import IdEntity


@dataclass
class BillingDataEntity:
    __name: str
    __government_id: str
    __email: str
    __debt_amount: float
    __debt_due_date: DateEntity
    __debt_id: IdEntity
    __status: str

    def __init__(
        self,
        name: str,
        government_id: str,
        email: str,
        debt_amount: float,
        debt_due_date: datetime,
        debt_id: IdEntity,
        status: str = None,
    ):
        self.__name = name
        self.__government_id = government_id
        self.__email = email
        self.__debt_amount = debt_amount
        self.__debt_due_date = debt_due_date
        self.__debtId = debt_id
        self.__status = status if status else "processed"

    @property
    def name(self) -> str:
        return self.__name

    @property
    def government_id(self) -> str:
        return self.__government_id

    @property
    def email(self) -> str:
        return self.__email

    @property
    def debt_amount(self) -> float:
        return self.__debt_amount

    @property
    def debt_due_date(self) -> str:
        return self.__debt_due_date.formated_date_without_time

    @property
    def debt_id(self) -> str:
        return self.__debtId.value

    @property
    def status(self) -> str:
        return self.__status
