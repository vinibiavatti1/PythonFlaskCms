"""
Builtin object module.
"""
from typing import Optional
from project.utils import validation_utils


class BuiltinObjectModel:
    """
    Builtin object model.
    """

    def __init__(self, *, name: str, object_type: str,
                 reference_name: Optional[str] = None,
                 properties: dict[str, str]) -> None:
        """
        Init builtin object model.
        """
        self.name = name
        self.object_type = object_type
        self.properties = properties
        self.reference_name = reference_name
