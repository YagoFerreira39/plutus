import uuid
from dataclasses import dataclass
from uuid import UUID


@dataclass
class IdEntity:
    __value: UUID

    def __init__(self, value: UUID):
        self.__value = value

    @property
    def value(self) -> str:
        return self.__value.hex

    @classmethod
    def new_one(cls) -> "IdEntity":
        return IdEntity(uuid.uuid4())

    @classmethod
    def of(cls, id: str) -> "IdEntity":
        return cls(uuid.UUID(hex=id, version=4))

    def __str__(self) -> str:
        return self.__value.hex
