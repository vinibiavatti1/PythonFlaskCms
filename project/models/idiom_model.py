"""
Idiom model.
"""


class IdiomModel:
    """
    Model of idiom property.
    """

    def __init__(self, code: str, name: str, default: bool) -> None:
        """
        Init idiom object.
        """
        self.code = code
        self.name = name
        self.default = default
