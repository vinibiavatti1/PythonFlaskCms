"""
Translation model.
"""
from project.utils import validation_utils


class TranslationModel:
    """
    Model with translation content.
    """

    def __init__(self, *, name: str, value: str) -> None:
        """
        Construct a translation model.
        """
        validation_utils.validate_name(name)
        self.name = name
        self.value = value
