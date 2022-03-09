"""
Label and Value model module.
"""


class LabelValueModel:
    """
    Label Value class.
    """

    def __init__(self, label: str, value: str) -> None:
        """
        Create a LabelValue model.
        """
        self.label = label
        self.value = value
