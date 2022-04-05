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
    def map_from_object_entity(cls, entity: ObjectEntity) -> 'UrlModel':
        """
        Create instance from ContentEntity.
        """
        return cls(
            url=entity.url,
            name=entity.name,
            resource_type=entity.object_type,
        )
