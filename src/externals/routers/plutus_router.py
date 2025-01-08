from fastapi import APIRouter
from starlette.routing import Router

from src.use_cases.data_types.router_requests.process_billing.process_billing_data_router_request import (
    ProcessBillingDataRouterRequest,
)


class PlutusRouter(Router):
    __plutus_router = APIRouter(prefix="/process-billing-data")

    @staticmethod
    def get_router() -> APIRouter:
        return PlutusRouter.__plutus_router

    @staticmethod
    @__plutus_router.post(
        path="/", tags=["Process Billing Data"], response_model_exclude_none=True
    )
    async def process_billing_data(router_request: ProcessBillingDataRouterRequest):
        pass
