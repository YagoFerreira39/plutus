from src.adapters.repositories.exceptions.repository_base_exception import (
    RepositoryBaseException,
)
from src.adapters.repositories.exceptions.repository_exceptions_reasons_enum import (
    RepositoryExceptionsReasonsEnum,
)


class RepositoryUnexpectedException(RepositoryBaseException):
    _reason = RepositoryExceptionsReasonsEnum.UNEXPECTED_EXCEPTION_ERROR


class ExtensionConversionException(RepositoryBaseException):
    _reason = RepositoryExceptionsReasonsEnum.EXTENSION_CONVERSION_EXCEPTION_ERROR


class FailToInsertInformationException(RepositoryBaseException):
    _reason = RepositoryExceptionsReasonsEnum.INSERT_EXCEPTION_ERROR


class FailToRetrieveInformationException(RepositoryBaseException):
    _reason = RepositoryExceptionsReasonsEnum.RETRIEVE_INFORMATION_EXCEPTION_ERROR
