"""
Page type module.
"""
from typing import Any, Union
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.utils import validation_utils


class PageTypeModel:
    """
    Page type model.
    """

    def __init__(self, *, label: str, name: str, template: str, icon: str,
                 properties: list[Union[HeaderModel, PropertyModel]]
                 ) -> None:
        """
        Init Page type model.
        """
        validation_utils.validate_name(name)
        self.label = label
        self.name = name
        self.template = template
        self.properties = properties
        self.icon = icon
