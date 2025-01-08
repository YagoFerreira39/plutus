from typing import TypedDict, List

from pydantic import BaseModel

from src.use_cases.data_types import base_model_omit_none
from src.use_cases.exceptions.use_case_exceptions_reasons_enum import (
    UseCaseExceptionsReasonsEnum,
)


@base_model_omit_none
class BaseApiResponse(BaseModel):
    status: bool
    error_code: UseCaseExceptionsReasonsEnum = None
    message: str = None
    payload: TypedDict | List[TypedDict] = None
