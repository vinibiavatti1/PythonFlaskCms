"""
Property model module.
"""
from project.utils import validation_utils


class PropertyModel:
    """
    Property class.
    """

    def __init__(
            self,
            *,
            name: str,
            label: str,
            property_type: str,
            description: str,
            placeholder: str = 'Property value',
            value: str = '',
            css_class: str = '',
            required: bool = False,
            enum_values: dict[str, str] = dict(),
            rows: str = '4',
            default: str = '') -> None:
        """
        Create property model.
        """
        validation_utils.validate_name(name)
        self.name = name
        self.label = label
        self.placeholder = placeholder
        self.value = value
        self.description = description
        self.property_type = property_type
        self.required = required
        self.enum_values = enum_values
        self.default = default
        self.value = ''
        self.css_class = css_class
        self.rows = rows
        if len(description) and self.description[-1] != '.':
            self.description += '.'
