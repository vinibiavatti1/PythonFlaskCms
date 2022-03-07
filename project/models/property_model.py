from typing import Optional


class PropertyModel:
    def __init__(self, name: str, description: str, field_type: str,
                 required: bool = False, values: list[str] = [],
                 default: Optional[str] = '') -> None:
        self.name = name
        self.description = description
        self.field_type = field_type
        self.required = required
        self.values = values
        self.default = default
