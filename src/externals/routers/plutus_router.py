from fastapi import APIRouter, UploadFile, File
from starlette.routing import Router

from src.adapters.controllers.process_billing_data_controller import (
    ProcessBillingDataController,
)
from src.use_cases.data_types.responses.process_billing_data_response import (
    ProcessBillingDataResponse,
)


class PlutusRouter(Router):
    __plutus_router = APIRouter(prefix="/process-billing-data")

    @staticmethod
    def get_router() -> APIRouter:
        return PlutusRouter.__plutus_router

    @staticmethod
    @__plutus_router.post(
        path="/",
        tags=["Process Billing Data"],
        response_model=ProcessBillingDataResponse,
        response_model_exclude_none=True,
    )
    async def process_billing_data(
        file: UploadFile = File(...),
    ) -> ProcessBillingDataResponse:
        response = await ProcessBillingDataController.process_billing(file=file)

        return response

    @staticmethod
    @__plutus_router.on_event("startup")
    async def send_billing_email() -> None:
        await ProcessBillingDataController.send_billing_email()