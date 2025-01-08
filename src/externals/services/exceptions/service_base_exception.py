from src.domain.exceptions.track_base_exception import TrackBaseException
from src.externals.services.exceptions.service_exceptions_reasons_enum import (
    ServiceExceptionsReasonsEnum,
)


class ServiceBaseException(TrackBaseException):
    _reason = ServiceExceptionsReasonsEnum
