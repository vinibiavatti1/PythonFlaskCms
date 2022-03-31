"""
URL model.
"""


from project.entities.object_entity import ObjectEntity


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

    @classmethod
    def map_from_content(cls, content: ObjectEntity) -> 'UrlModel':
        """
        Create instance from ContentEntity.
        """
        return cls(
            url=content.url,
            name=content.name,
            resource_type=content.object_type,
        )
