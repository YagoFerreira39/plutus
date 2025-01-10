from src.use_cases.data_types.responses.base.base_api_response import BaseApiResponse

from src.use_cases.data_types import base_model_omit_none
from src.use_cases.data_types.responses.payloads.process_billing_data_payload import (
    ProcessBillingDataPayload,
)


@base_model_omit_none
class ProcessBillingDataResponse(BaseApiResponse):
    payload: ProcessBillingDataPayload = None
