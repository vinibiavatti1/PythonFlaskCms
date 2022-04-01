"""
Resource type module.
"""
from typing import Union
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.utils import validation_utils


class ResourceTypeModel:
    """
    Resource type model.
    """

    def __init__(self, *, label: str, name: str, icon: str,
                 properties: list[Union[HeaderModel, PropertyModel]],
                 ) -> None:
        """
        Init Resource type model.
        """
        validation_utils.validate_name(name)
        self.label = label
        self.name = name
        self.properties = properties
        self.icon = icon
