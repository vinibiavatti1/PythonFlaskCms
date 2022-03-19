"""
Validator for auth data module.
"""
from typing import Any
from project.utils.validation_utils import validate_form_data_fields


def validate_login_data(form_data: dict[str, Any]) -> None:
    """
    Validate login data.
    """
    validate_form_data_fields(
        form_data,
        'email',
        'password',
        'context',
    )
