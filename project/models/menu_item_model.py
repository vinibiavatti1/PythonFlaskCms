"""
Menu model.
"""


class MenuItemModel:
    """
    Model of menu property.
    """

    def __init__(self, *, title: str, link: str, icon: str,
                 target: str = '', badge_id: str = '') -> None:
        """
        Init menu object.
        """
        self.title = title
        self.link = link
        self.icon = icon
        self.target = target
        self.context = ''
        self.badge_id = badge_id
