from enum import IntEnum


class HttpSessionInfrastructureExceptionsReasonsEnum(IntEnum):
    # TransportInfrastructureExceptionCodes 800-899

    UNEXPECTED_ERROR = 801
    RUNTIME_ERROR = 802
    INVALID_URL_ERROR = 803
    SERVER_TIMEOUT_ERROR = 804
    CLIENT_OS_ERROR = 805
    TOO_MANY_REDIRECTS = 806
