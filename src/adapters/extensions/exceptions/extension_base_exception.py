from uuid import UUID

from src.adapters.extensions.exceptions.extension_exceptions_reasons_enum import (
    ExtensionExceptionsReasonsEnum,
)
from src.domain.exceptions.track_base_exception import TrackBaseException


class ExtensionBaseException(TrackBaseException):
    _reason = ExtensionExceptionsReasonsEnum

    def __init__(
        self,
        message: str,
        reason: ExtensionExceptionsReasonsEnum = None,
        error_id: UUID = None,
        original_error: Exception = None,
    ):
        super().__init__(
            message=message,
            reason=reason,
            error_id=error_id,
            original_error=original_error,
        )
