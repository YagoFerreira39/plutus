from src.domain.exceptions.entity_base_exception import EntityBaseException
from src.domain.exceptions.entity_exceptions_reasons_enum import (
    EntityExceptionsReasonsEnum,
)


class UnableToProcessBillingDataException(EntityBaseException):
    _reason = EntityExceptionsReasonsEnum.UNABLE_TO_PROCESS_BILLING_DATA_ERROR


class UnableToFormatDatePatternError(EntityBaseException):
    _reason = EntityExceptionsReasonsEnum.UNABLE_TO_FORMAT_DATE_PATTERN_ERROR
