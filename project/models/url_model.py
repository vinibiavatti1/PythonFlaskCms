"""
URL model.
"""


class UrlModel:
    """
    Model of URL property.
    """

    def __init__(self, *, url: str, name: str, resource_type: str) -> None:
        """
        Init URL object.
        """
        self.url = url
        self.name = name
        self.resource_type = resource_type
