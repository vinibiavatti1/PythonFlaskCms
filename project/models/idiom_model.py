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
        if len(code) != 2:
            raise ValueError(
                f'Idiom code must have exactly two characters, '
                f'but has: {len(code)} characters. Idiom code: {code}'
            )
        self.code = code
        self.name = name
        self.default = default
