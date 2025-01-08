from enum import IntEnum


class ServiceExceptionsReasonsEnum(IntEnum):
    # ServiceExceptionsCodes 500-599

    UNEXPECTED_EXCEPTION = 500
    HTTP_SERVICE_EXCEPTION = 501
    FAIL_TO_SEND_EMAIL_ERROR = 502
