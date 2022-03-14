"""
Block module.
"""
from project.models.property_model import PropertyModel
import re


class BlockModel:
    """
    block model.
    """

    def __init__(self, *, name: str, description: str, template: str,
                 properties: list[PropertyModel]) -> None:
        """
        Init block model.
        """
        if not re.match(r'^[a-z\_]+$', name):
            raise ValueError(f'Property name is invalid: "{name}"')
        self.name = name
        self.description = description
        self.properties = properties
        self.template = template

