"""
Validaton utilities module.
"""
from typing import Any
from project.errors import ValidationError
import re


def validate_form_data_fields(form_data: dict[str, Any], *fields: str) -> None:
    """
    Check required form data fields.
    """
    for field in fields:
        if field not in form_data:
            raise ValidationError(f'"{field.title()}" is required')


def validate_name(name: str) -> None:
    """
    Validates if name is a valid name for admin.
    """
    if re.match(r'^[a-z_]+$', name) is None:
        raise ValidationError(
            'The name is invalid. It supports low characters and "_" as '
            'separator only'
        )
