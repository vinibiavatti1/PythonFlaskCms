"""
Menu model.
"""


class MenuModel:
    """
    Model of menu property.
    """

    def __init__(self, *, title: str, link: str, icon: str,
                 target: str = '') -> None:
        """
        Init menu object.
        """
        self.title = title
        self.link = link
        self.icon = icon
        self.target = target
