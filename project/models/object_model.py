"""
Object model class.
"""
from typing import Optional, Union
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.utils import validation_utils
from project.properties.main_properties import main_properties
from copy import deepcopy


class ObjectModel:
    """
    Object model.
    """

    def __init__(self, *,
                 name: str,
                 description: str,
                 icon: str,
                 properties: list[Union[HeaderModel, PropertyModel]],
                 is_root: bool = False,
                 is_content: bool = True,
                 children: list[str] = [],
                 allow_actions: bool = True,
                 template: Optional[str] = None,
                 ) -> None:
        """
        Init object model.
        """
        self.name = name
        self.template = template
        self.description = description
        self.allow_actions = allow_actions
        self.children = children
        self.properties = deepcopy(main_properties)
        self.properties.extend(properties)
        self.icon = icon
        self.is_content = is_content
        self.is_root = is_root
        if is_content and not template:
            raise ValueError('Content objects require a template name')
