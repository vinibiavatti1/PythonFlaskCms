"""
Validaton utilities module.
"""
from typing import Any
from project.errors import ValidationError


def validate_form_data_fields(form_data: dict[str, Any], *fields: str) -> None:
    """
    Check required form data fields.
    """
    for field in fields:
        if field not in form_data:
            raise ValidationError(f'"{field.title()}" is required')
