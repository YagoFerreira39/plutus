from typing import Optional

from fastapi import APIRouter, UploadFile, File
from pydantic import BaseModel
from starlette.routing import Router

class PlutusRouter(Router):
    __plutus_router = APIRouter(prefix="/process-billing-data")

    @staticmethod
    def get_router() -> APIRouter:
        return PlutusRouter.__plutus_router

    @staticmethod
    @__plutus_router.post(
        path="/", tags=["Process Billing Data"], response_model_exclude_none=True
    )
    async def process_billing_data(file: UploadFile = File(...)) -> dict:
        pass
