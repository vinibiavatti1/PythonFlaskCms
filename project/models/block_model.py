"""
Block module.
"""
from project.models.property_model import PropertyModel
from project.utils import validation_utils


class BlockModel:
    """
    block model.
    """

    def __init__(self, *, name: str, description: str, template: str,
                 properties: list[PropertyModel]) -> None:
        """
        Init block model.
        """
        validation_utils.validate_name(name)
        self.name = name
        self.description = description
        self.properties = properties
        self.template = template

