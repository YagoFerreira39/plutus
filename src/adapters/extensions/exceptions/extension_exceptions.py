from src.adapters.extensions.exceptions.extension_exceptions_reasons_enum import (
    ExtensionExceptionsReasonsEnum,
)
from src.adapters.extensions.exceptions.extension_base_exception import (
    ExtensionBaseException,
)


class ExtensionUnexpectedException(ExtensionBaseException):
    _reason = ExtensionExceptionsReasonsEnum.UNEXPECTED_EXCEPTION
