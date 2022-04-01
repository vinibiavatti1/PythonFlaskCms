"""
Record utilities.
"""
from typing import Any, Optional


def get_record_by_name(name: str, record_list: list[Any]
                       ) -> Optional[Any]:
    """
    Generic function to get record by name.
    """
    for record in record_list:
        if hasattr(record, 'name') and getattr(record, 'name') == name:
            return record
    return None
