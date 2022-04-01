"""
Content type module.
"""
from typing import Union
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.utils import validation_utils


class ContentTypeModel:
    """
    Content type model.
    """

    def __init__(self, *, label: str, name: str, template: str, icon: str,
                 properties: list[Union[HeaderModel, PropertyModel]],
                 allow_blocks: bool = False,
                 ) -> None:
        """
        Init Content type model.
        """
        validation_utils.validate_name(name)
        self.label = label
        self.name = name
        self.template = template
        self.allow_blocks = allow_blocks
        self.properties = properties
        self.icon = icon
