"""
Page model.
"""
from project.enums import resource_type_enum


class PageModel:
    """
    Model of Page property.
    """

    def __init__(self, *, name: str) -> None:
        """
        Init Page object.
        """
        self.name = name
        self.resource_type = resource_type_enum.PAGE
        self.published = 1
