from src.externals.services.exceptions.service_base_exception import (
    ServiceBaseException,
)
from src.externals.services.exceptions.service_exceptions_reasons_enum import (
    ServiceExceptionsReasonsEnum,
)


class ServiceUnexpectedException(ServiceBaseException):
    _reason = ServiceExceptionsReasonsEnum.UNEXPECTED_EXCEPTION


class HttpServiceException(ServiceBaseException):
    _reason = ServiceExceptionsReasonsEnum.HTTP_SERVICE_EXCEPTION


class FailToSendEmailException(ServiceBaseException):
    _reason = ServiceExceptionsReasonsEnum.FAIL_TO_SEND_EMAIL_ERROR
