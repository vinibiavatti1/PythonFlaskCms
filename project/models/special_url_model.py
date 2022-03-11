"""
Special url model.
"""


class SpecialUrlModel:
    """
    Special url model.
    """

    def __init__(self, url: str, sitemap_priority: float,
                 sitemap_change_frequently: str, sitemap_active: bool) -> None:
        """
        Init special url model object.
        """
        self.url = url
        self.sitemap_priority = sitemap_priority
        self.sitemap_change_frequently = sitemap_change_frequently
        self.sitemap_active = sitemap_active
