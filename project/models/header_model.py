"""
Generic header module.
"""


class HeaderModel:
    """
    Header model.
    """

    def __init__(self, title: str) -> None:
        """
        Init header model.
        """
        self.title = title
        self.header = True

