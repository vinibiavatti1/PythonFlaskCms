"""
Record type module.
"""
from typing import Optional, Union
from project.models.property_model import PropertyModel
from project.models.header_model import HeaderModel
from project.utils import validation_utils


class RecordTypeModel:
    """
    Record type model.
    """

    def __init__(self, *, label: str, name: str, icon: str,
                 properties: list[Union[HeaderModel, PropertyModel]],
                 allow_deleted: bool = True,
                 allow_duplicated: bool = True,
                 nested_objects: list[str] = [],
                 template: Optional[str] = None,
                 ) -> None:
        """
        Init Record type model.
        """
        validation_utils.validate_name(name)
        self.label = label
        self.name = name
        self.template = template
        self.allow_deleted = allow_deleted
        self.allow_duplicated = allow_duplicated
        self.nested_objects = nested_objects
        self.properties = properties
        self.icon = icon
