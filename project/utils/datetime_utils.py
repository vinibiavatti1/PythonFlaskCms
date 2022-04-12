"""
Date and Datetime utils module.
"""
from typing import Any, Optional
from datetime import date, datetime
from project.services import property_service


###############################################################################
# Constants
###############################################################################


HTML_DATE_FORMAT = '%Y-%m-%d'
HTML_DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S'


###############################################################################
# Functions
###############################################################################


def format_date_to_str(date_: date, *,
                       html_format: bool = False,
                       config_format: bool = False,
                       context: Optional[str] = None,
                       custom_format: Optional[str] = None) -> str:
    """
    Format date to string.

    Args:
        date: date object
        **html_format: Use the HTML date format
        **config_format: Use the admin configuration date format
        **custom_format: Use a custom format
    """
    if html_format:
        return date_.strftime(HTML_DATE_FORMAT)
    elif config_format:
        if context is None:
            raise ValueError('Context must be set when config_format is True')
        date_format = property_service.get_property_value(
            context,
            'date_format'
        )
        return date_.strftime(date_format)
    elif custom_format:
        return date_.strftime(custom_format)
    else:
        raise ValueError('A format must be selected to format the date')


def format_datetime_to_str(datetime_: datetime, *,
                           html_format: bool = False,
                           config_format: bool = False,
                           context: Optional[str] = None,
                           custom_format: Optional[str] = None) -> str:
    """
    Format datetime to string.

    Args:
        datetime: datetime object
        **html_format: Use the HTML datetime format
        **config_format: Use the admin configuration datetime format
        **custom_format: Use a custom format
    """
    if html_format:
        return datetime_.strftime(HTML_DATETIME_FORMAT)
    elif config_format:
        if context is None:
            raise ValueError('Context must be set when config_format is True')
        date_format = property_service.get_property_value(
            context,
            'datetime_format'
        )
        return datetime_.strftime(date_format)
    elif custom_format:
        return datetime_.strftime(custom_format)
    else:
        raise ValueError('A format must be selected to format the date')


def convert_datetime_to_timestamp(data: dict[str, Any]) -> dict[str, Any]:
    """
    Convert datetime values to timestamp.
    """
    for key in data.keys():
        if isinstance(data[key], (datetime, date)):
            data[key] = data[key].timestamp()
    return data


def convert_list_datetime_to_timestamp(data: list[dict[str, Any]]
                                       ) -> list[dict[str, Any]]:
    """
    Convert datetime values to timestamp in list.
    """
    for index in range(len(data)):
        data[index] = convert_datetime_to_timestamp(data[index])
    return data
