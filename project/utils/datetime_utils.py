"""
Date and Datetime utils module.
"""
from typing import Optional
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
        date_format = property_service.get_property('date_format')
        return date_.strftime(date_format)
    elif custom_format:
        return date_.strftime(custom_format)
    else:
        raise ValueError('A format must be selected to format the date')


def format_datetime_to_str(datetime_: datetime, *,
                           html_format: bool = False,
                           config_format: bool = False,
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
        date_format = property_service.get_property('datetime_format')
        return datetime_.strftime(date_format)
    elif custom_format:
        return datetime_.strftime(custom_format)
    else:
        raise ValueError('A format must be selected to format the date')
