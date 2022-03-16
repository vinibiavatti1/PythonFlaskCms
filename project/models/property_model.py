"""
Property model module.
"""
from typing import Any, Optional
from project.utils import validation_utils


class PropertyModel:
    """
    Property class.
    """

    def __init__(self, *, name: str, field_type: str, description: str = '',
                 required: bool = False, values: list[str] = [],
                 default: Optional[Any] = '') -> None:
        """
        Create property model.

        The name must be unique, and follow the /[a-z_]+/ pattern.
        """
        validation_utils.validate_name(name)
        self.name = name
        self.description = description
        self.field_type = field_type
        self.required = required
        self.values = values
        self.default = default
        self.value = ''
        if isinstance(self.default, bool):
            self.default = '1' if self.default else '0'
