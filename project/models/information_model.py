"""
Information module.
"""


class InformationModel:
    """
    Information model.
    """

    def __init__(self, *, name: str, description: str, value: str) -> None:
        """
        Init information model.
        """
        self.name = name
        self.description = description
        self.value = value
