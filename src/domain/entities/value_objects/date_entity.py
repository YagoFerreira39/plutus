import datetime
import re

from src.domain.exceptions.entity_exceptions import UnableToFormatDatePatternError


class DateEntity:
    def __init__(self, date: datetime):
        self.__date = date

    @property
    def date(self) -> datetime:
        return self.__date

    @property
    def formated_date_with_time(self) -> str:
        self.__convert_to_datetime_object()
        formated_date_with_time = self.__format_date_with_time()
        return formated_date_with_time

    @property
    def formated_date_without_time(self) -> str:
        self.__convert_to_datetime_object()
        formated_date_without_time = self.__format_date()
        return formated_date_without_time

    @classmethod
    def of(cls, date_str: str, date_format: str = "%Y-%m-%d"):
        return cls(date=datetime.datetime.strptime(date_str, date_format))

    def __format_date_with_time(self) -> str:
        try:
            formatted_date = None
            if self.__date:
                str_date = str(self.__date)
                microsecond_pattern = re.compile(r"\.\d+")

                if microsecond_pattern.search(str_date):
                    datetime_format = "%Y-%m-%d %H:%M:%S.%f"
                else:
                    datetime_format = "%Y-%m-%d %H:%M:%S"

                datetime_obj = datetime.datetime.strptime(str_date, datetime_format)
                formatted_date = datetime_obj.strftime("%d/%m/%Y %H:%M:%S")

            return formatted_date

        except Exception as original_exception:
            raise UnableToFormatDatePatternError(
                message="Unable to format date pattern.",
                original_error=original_exception,
            ) from original_exception

    def __format_date(self) -> str:
        try:
            formatted_date = None
            if self.__date:
                str_date = str(self.__date)

                datetime_obj = datetime.datetime.strptime(
                    str_date, format("%Y-%m-%d %H:%M:%S")
                )
                formatted_date = datetime_obj.strftime("%d/%m/%Y")

            return formatted_date

        except Exception as original_exception:
            raise UnableToFormatDatePatternError(
                message="Unable to format date pattern.",
                original_error=original_exception,
            ) from original_exception

    def __convert_to_datetime_object(self) -> None:
        try:
            if type(self.__date) is int or type(self.__date) is float:
                self.__date = datetime.datetime.fromtimestamp(self.__date)
        except Exception as original_exception:
            raise UnableToFormatDatePatternError(
                message="Unable to convert to datetime object.",
                original_error=original_exception,
            ) from original_exception
