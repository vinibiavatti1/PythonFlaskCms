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
