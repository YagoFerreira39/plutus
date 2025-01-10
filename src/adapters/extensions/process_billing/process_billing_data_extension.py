import csv
from io import StringIO

from fastapi import UploadFile

from src.adapters.extensions.exceptions.extension_exceptions import (
    ExtensionUnexpectedException,
)
from src.domain.entities.billing_data_entity import BillingDataEntity

from src.domain.entities.billing_file_entity import BillingFileEntity
from src.domain.entities.value_objects.date_entity import DateEntity
from src.domain.entities.value_objects.id_entity import IdEntity
from src.domain.models.billing_data_model import BillingDataModel
from src.use_cases.data_types.dtos.process_billing.process_billing_data_dto import (
    ProcessBillingDataDto,
)
from src.use_cases.data_types.requests.process_billing.process_billing_data_request import (
    ProcessBillingDataRequest,
)
from src.use_cases.data_types.responses.payloads.process_billing_data_payload import (
    ProcessBillingDataPayload,
)
from src.use_cases.data_types.responses.process_billing_data_response import (
    ProcessBillingDataResponse,
)
from src.use_cases.ports.extensions.process_billing.i_process_billing_data_extension import (
    IProcessBillingDataExtension,
)


class ProcessBillingDataExtension(IProcessBillingDataExtension):

    @staticmethod
    def from_result_to_model(result: dict) -> BillingDataModel:
        try:
            model = BillingDataModel(
                name=result.get("name"),
                government_id=result.get("government_id"),
                email=result.get("email"),
                debt_amount=result.get("debt_amount"),
                debt_due_date=result.get("debt_due_date"),
                debt_id=result.get("debt_id"),
                status=result.get("status"),
                billing_id=str(result.get("_id")),
            )

            return model

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_result_list_to_model_list(
        result_list: list[dict],
    ) -> list[BillingDataModel]:
        try:
            model_list = [
                ProcessBillingDataExtension.from_result_to_model(result=result)
                for result in result_list
            ]

            return model_list

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_router_request_to_request(
        file: UploadFile,
    ) -> ProcessBillingDataRequest:
        try:
            request = ProcessBillingDataRequest(file=file)

            return request

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    async def from_request_to_entity(
        request: ProcessBillingDataRequest,
    ) -> BillingFileEntity:
        try:
            content = await request.file.read()
            csv_data = StringIO(content.decode("utf-8"))

            reader = csv.DictReader(csv_data)
            billing_data_list = []
            for row in reader:
                billing_data = BillingDataEntity(
                    name=row["name"],
                    government_id=row["governmentId"],
                    email=row["email"],
                    debt_amount=float(row["debtAmount"]),
                    debt_due_date=DateEntity.of(row["debtDueDate"]),
                    debt_id=IdEntity.of(row["debtId"]),
                )

                billing_data_list.append(billing_data)

            entity = BillingFileEntity(
                content_type=request.file.content_type, data=billing_data_list
            )

            return entity

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_entity_list_to_model_list(
        entity_list: list[BillingDataEntity],
    ) -> list[BillingDataModel]:
        try:
            model_list = [
                BillingDataModel(
                    name=entity.name,
                    government_id=entity.government_id,
                    email=entity.email,
                    debt_amount=entity.debt_amount,
                    debt_due_date=entity.debt_due_date,
                    debt_id=entity.debt_id,
                    status=entity.status,
                )
                for entity in entity_list
            ]

            return model_list

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_model_list_to_dto(
        model_list: list[BillingDataModel],
    ) -> ProcessBillingDataDto:
        try:
            dto = ProcessBillingDataDto(total=len(model_list))

            return dto

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception

    @staticmethod
    def from_dto_to_response(dto: ProcessBillingDataDto) -> ProcessBillingDataResponse:
        try:
            payload = ProcessBillingDataPayload(total=dto.total)

            response = ProcessBillingDataResponse(
                status=True, payload=payload, message="Billing data processed with success"
            )

            return response

        except Exception as original_exception:
            raise ExtensionUnexpectedException(
                message="Unexpected extension exception.",
                original_error=original_exception,
            ) from original_exception
