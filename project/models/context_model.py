"""
Context model.
"""


class ContextModel:
    """
    Model of context property.
    """

    def __init__(self, *, code: str, name: str, description: str,
                 default: bool) -> None:
        """
        Init context object.
        """
        self.code = code
        self.name = name
        self.description = description
        self.default = default

    def __str__(self) -> str:
        """
        Return code when converted to str.
        """
        return self.code

    def __repr__(self) -> str:
        """
        Return code when represented.
        """
        return self.code
