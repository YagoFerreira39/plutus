from uuid import UUID

from src.domain.exceptions.track_base_exception import TrackBaseException
from src.use_cases.exceptions.use_case_exceptions_reasons_enum import (
    UseCaseExceptionsReasonsEnum,
)


class UseCaseBaseException(TrackBaseException):
    _reason = UseCaseExceptionsReasonsEnum

    def __init__(
        self,
        message: str,
        reason: UseCaseExceptionsReasonsEnum = None,
        error_id: UUID = None,
        original_error: Exception = None,
    ):
        super().__init__(
            message=message,
            reason=reason,
            error_id=error_id,
            original_error=original_error,
        )
