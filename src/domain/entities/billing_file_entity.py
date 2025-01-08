from dataclasses import dataclass

from src.domain.entities.billing_data_entity import BillingDataEntity
from src.domain.exceptions.entity_exceptions import UnableToProcessBillingDataException


@dataclass
class BillingFileEntity:
    __content_type: str
    __data: list[BillingDataEntity]

    def __init__(self, content_type: str, data: list[BillingDataEntity]):
        self.__content_type = content_type
        self.__data = data
        self.__create()

    @property
    def content_type(self) -> str:
        return self.__content_type

    @property
    def data(self) -> list[BillingDataEntity]:
        return self.__data

    def __create(self):
        self.__validate_content_type()

    def __validate_content_type(self) -> None:
        if self.__content_type != "text/csv":
            raise UnableToProcessBillingDataException(
                message="unable to process billing data"
            )
