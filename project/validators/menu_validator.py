"""
Menu Validator.

This module provides validator for menu data.
"""
from typing import Any
from project.utils import validation_utils


def validate_save_data(form_data: dict[str, Any]) -> None:
    """
    Validate page insert data.
    """
    validation_utils.validate_form_data_fields(
        form_data,
        'name',
        'json',
        'idiom',
    )
    validation_utils.validate_name(str(form_data.get('name')))
