"""
Translation Validator.

This module provides validations for translation data.
"""
from typing import Any
from project.utils import validation_utils


def validate_save_data(form_data: dict[str, Any]) -> None:
    """
    Validate translation insert data.
    """
    validation_utils.validate_form_data_fields(
        form_data,
        'name',
        'value',
        'idiom',
    )
    validation_utils.validate_name(str(form_data.get('name')))
