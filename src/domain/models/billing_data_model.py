import datetime
from dataclasses import dataclass


@dataclass(slots=True)
class BillingDataModel:
    name: str
    government_id: str
    email: str
    debt_amount: float
    debt_due_date: datetime
    debt_id: str
    status: str
    created_at: datetime = None
    updated_at: datetime = None
    billing_id: str = None

    def __as_dict(self) -> dict:
        model_dict = {
            "name": self.name,
            "government_id": self.government_id,
            "email": self.email,
            "debt_amount": self.debt_amount,
            "debt_due_date": self.debt_due_date,
            "debt_id": self.debt_id,
            "status": self.status,
        }

        return model_dict

    def to_insert(self) -> dict:
        model_to_insert = self.__as_dict()
        model_to_insert["created_at"] = datetime.datetime.strftime(
            datetime.datetime.now(), "%Y-%m-%d %H:%M:%S"
        )
        model_to_insert["updated_at"] = datetime.datetime.strftime(
            datetime.datetime.now(), "%Y-%m-%d %H:%M:%S"
        )

        return model_to_insert

    @staticmethod
    def to_update_status() -> dict:
        to_update = {
            "status": "sent",
            "updated_at": datetime.datetime.now(tz=datetime.timezone.utc),
        }

        return to_update
