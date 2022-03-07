"""
Menu model.
"""


class MenuModel:
    """
    Model of menu property.
    """

    def __init__(self, title: str, link: str, icon: str) -> None:
        """
        Init menu object.
        """
        self.title = title
        self.link = link
        self.icon = icon
