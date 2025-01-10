from bson import ObjectId
from decouple import config
from motor.motor_asyncio import AsyncIOMotorClientSession

from src.adapters.repositories.exceptions.repository_exceptions import (
    FailToInsertInformationException,
    FailToRetrieveInformationException,
)
from src.externals.infrastructure.mongo_db.exceptions.mongo_db_base_infrastructure_exception import (
    MongoDbBaseInfrastructureException,
)

from src.adapters.ports.infrastructure.mongo_db.i_mongo_db_collection import (
    IMongoDbCollection,
)

from src.adapters.ports.infrastructure.mongo_db.i_mongo_db_infrastructure import (
    IMongoDbInfrastructure,
)

from witch_doctor import WitchDoctor

from src.domain.models.billing_data_model import BillingDataModel
from src.use_cases.ports.extensions.process_billing.i_process_billing_data_extension import (
    IProcessBillingDataExtension,
)
from src.use_cases.ports.repositories.mongo_db.i_billing_data_repository import (
    IBillingDataRepository,
)


class BillingDataRepository(IBillingDataRepository):
    __mongo_db_infrastructure: IMongoDbInfrastructure
    __collection: IMongoDbCollection
    __process_billing_data_extension: IProcessBillingDataExtension

    @WitchDoctor.injection
    def __init__(
        self,
        mongo_db_infrastructure: IMongoDbInfrastructure,
        process_billing_data_extension: IProcessBillingDataExtension,
    ):
        BillingDataRepository.__mongo_db_infrastructure = mongo_db_infrastructure
        BillingDataRepository.__collection = (
            BillingDataRepository.__mongo_db_infrastructure.require_collection(
                database=config("PLUTUS_DATABASE"),
                collection=config("BILLING_DATA_COLLECTION"),
            )
        )
        BillingDataRepository.__process_billing_data_extension = (
            process_billing_data_extension
        )

    @classmethod
    async def register_billing_data_batch(
        cls, billing_data_model_list: list[BillingDataModel]
    ) -> None:
        session: AsyncIOMotorClientSession = (
            await cls.__mongo_db_infrastructure.get_client().start_session()
        )

        try:
            documents_to_insert = [
                model.to_insert() for model in billing_data_model_list
            ]

            async with session.start_transaction():
                async with cls.__collection.with_collection() as collection:
                    await collection.insert_many(documents_to_insert)

        except MongoDbBaseInfrastructureException as original_exception:
            raise FailToInsertInformationException(
                message="Failed to insert billing data in database.",
                original_error=original_exception,
            ) from original_exception

    @classmethod
    async def get_billing_data_by_debt_ids(
        cls, debt_ids: list[str]
    ) -> list[BillingDataModel]:
        try:
            async with cls.__collection.with_collection() as collection:
                step = 5000
                start = 0
                result_list = []

                for size in range(start, len(debt_ids), step):
                    debt_ids_to_query = debt_ids[size : size + step]

                    query = {"debt_id": {"$in": debt_ids_to_query}}

                    result = (
                        await collection.find(query).limit(step).to_list(length=None)
                    )

                    model_list = cls.__process_billing_data_extension.from_result_list_to_model_list(
                        result_list=result
                    )

                    result_list.extend(model_list)

                return result_list
        except MongoDbBaseInfrastructureException as original_exception:
            raise FailToRetrieveInformationException(
                message="Failed to retrieve billing data in database.",
                original_error=original_exception,
            ) from original_exception

    @classmethod
    async def get_billing_data_by_status(cls, status: str) -> list[BillingDataModel]:
        try:
            async with cls.__collection.with_collection() as collection:
                query = {"status": status}

                result_list = (
                    await collection.find(query).limit(20).to_list(length=None)
                )

                model_list = (
                    cls.__process_billing_data_extension.from_result_list_to_model_list(
                        result_list=result_list
                    )
                )

                return model_list

        except MongoDbBaseInfrastructureException as original_exception:
            raise FailToRetrieveInformationException(
                message="Failed to retrieve billing data in database.",
                original_error=original_exception,
            ) from original_exception

    @classmethod
    async def update_billing_data_status(
        cls, billing_data_model: BillingDataModel
    ) -> None:
        try:
            async with cls.__collection.with_collection() as collection:
                to_update = billing_data_model.to_update_status()

                await collection.update_one(
                    {"_id": ObjectId(billing_data_model.billing_id)},
                    {"$set": {**to_update}},
                )

        except MongoDbBaseInfrastructureException as original_exception:
            raise FailToInsertInformationException(
                message="Failed to insert billing data in database.",
                original_error=original_exception,
            ) from original_exception
