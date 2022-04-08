"""
Builtin object module.
"""
from project.utils import validation_utils


class BuiltinObjectModel:
    """
    Builtin object model.
    """

    def __init__(self, *, name: str, object_type: str, object_subtype: str,
                 properties: dict[str, str]) -> None:
        """
        Init builtin object model.
        """
        validation_utils.validate_name(name)
        self.name = name
        self.object_type = object_type
        self.object_subtype = object_subtype
        self.properties = properties

