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

    def __init__(self, *, name: str, template: str, allow_blocks: bool,
                 properties: list[Union[HeaderModel, PropertyModel]],
                 ) -> None:
        """
        Init Content type model.
        """
        validation_utils.validate_name(name)
        self.name = name
        self.template = template
        self.allow_blocks = allow_blocks
        self.properties = properties

