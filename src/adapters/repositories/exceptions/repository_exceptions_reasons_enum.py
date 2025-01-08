from enum import IntEnum


class RepositoryExceptionsReasonsEnum(IntEnum):
    # ExtensionExceptionsCodes  200-299

    RETRIEVE_INFORMATION_EXCEPTION_ERROR = 200
    INSERT_EXCEPTION_ERROR = 201
    EXTENSION_CONVERSION_EXCEPTION_ERROR = 202
    UNEXPECTED_EXCEPTION_ERROR = 203
