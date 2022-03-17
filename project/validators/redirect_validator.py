"""
Redirect Validator.

This module provides validations for redirect data.
"""
from typing import Any
from project.utils import validation_utils


def validate_save_data(form_data: dict[str, Any]) -> None:
    """
    Validate redirect insert data.
    """
    validation_utils.validate_form_data_fields(
        form_data,
        'from_url',
        'to_url',
        'from_url_regex',
    )
