from fastapi import UploadFile
from witch_doctor import WitchDoctor

from src.adapters.controllers import controller_error_handler
from src.use_cases.data_types.responses.process_billing_data_response import (
    ProcessBillingDataResponse,
)
from src.use_cases.ports.extensions.process_billing.i_process_billing_data_extension import (
    IProcessBillingDataExtension,
)
from src.use_cases.ports.use_cases.i_process_billing_data_use_case import (
    IProcessBillingDataUseCase,
)
from src.use_cases.ports.use_cases.i_send_billing_email_use_case import ISendBillingEmailUseCase


class ProcessBillingDataController:
    @classmethod
    @controller_error_handler
    @WitchDoctor.injection
    async def process_billing(
        cls,
        file: UploadFile,
        process_billing_data_extension: IProcessBillingDataExtension,
        process_billing_data_use_case: IProcessBillingDataUseCase,
    ) -> ProcessBillingDataResponse:
        request = process_billing_data_extension.from_router_request_to_request(
            file=file
        )

        use_case_response = await process_billing_data_use_case.execute(request=request)

        response = process_billing_data_extension.from_dto_to_response(
            dto=use_case_response
        )

        return response
    
    @classmethod
    @controller_error_handler
    @WitchDoctor.injection
    async def send_billing_email(
        cls,
        process_billing_data_extension: IProcessBillingDataExtension,
        send_billing_email_use_case: ISendBillingEmailUseCase,
    ) -> None:
        await send_billing_email_use_case.send_pending_billings()
