from src.externals.infrastructure.http_config.exceptions.http_session_infrastructure_base_exception import (
    HttpSessionInfrastructureBaseException,
)
from src.externals.infrastructure.http_config.exceptions.http_session_infrastructure_exceptions_reasons_enum import (
    HttpSessionInfrastructureExceptionsReasonsEnum,
)


class HttpSessionInfrastructureUnexpectedException(
    HttpSessionInfrastructureBaseException
):
    _reason = HttpSessionInfrastructureExceptionsReasonsEnum.UNEXPECTED_ERROR


class HttpSessionInfrastructureRuntimeErrorException(
    HttpSessionInfrastructureBaseException
):
    _reason = HttpSessionInfrastructureExceptionsReasonsEnum.RUNTIME_ERROR


class HttpSessionInfrastructureInvalidUrlErrorException(
    HttpSessionInfrastructureBaseException
):
    _reason = HttpSessionInfrastructureExceptionsReasonsEnum.INVALID_URL_ERROR


class HttpSessionInfrastructureServerTimeoutErrorException(
    HttpSessionInfrastructureBaseException
):
    _reason = HttpSessionInfrastructureExceptionsReasonsEnum.SERVER_TIMEOUT_ERROR


class HttpSessionInfrastructureClientOSErrorException(
    HttpSessionInfrastructureBaseException
):
    _reason = HttpSessionInfrastructureExceptionsReasonsEnum.CLIENT_OS_ERROR


class HttpSessionInfrastructureTooManyRedirectsErrorException(
    HttpSessionInfrastructureBaseException
):
    _reason = HttpSessionInfrastructureExceptionsReasonsEnum.TOO_MANY_REDIRECTS
