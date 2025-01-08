from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from src.use_cases.data_types.responses.base.base_api_response import BaseApiResponse
from src.use_cases.exceptions.use_case_base_exception import UseCaseBaseException
from src.use_cases.ports.extensions.i_base_controller_extension import (
    IBaseControllerExtension,
)


class BaseControllerExtension(IBaseControllerExtension):
    @staticmethod
    def create_error_response(
        exception: UseCaseBaseException,
    ) -> JSONResponse:
        api_response = BaseApiResponse(
            status=False,
            error_code=exception.reason,
            message=exception.message,
        )

        encoded_api_response = jsonable_encoder(api_response)

        response = JSONResponse(
            status_code=exception.http_status_code, content=encoded_api_response
        )

        return response
