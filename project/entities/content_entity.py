"""
Content entity.

Model to map database content entity.
"""
from typing import Any, Optional
from datetime import datetime
import json


class ContentEntity:
    """
    Content entity class.
    """

    def __init__(self, *,
                 id: int = -1,
                 context: str,
                 name: str,
                 resource_type: str,
                 data: dict[str, Any] = dict(),
                 created_on: datetime = datetime.now(),
                 deleted: bool = False,
                 deleted_on: Optional[datetime] = None
                 ) -> None:
        """
        Init content entity object.
        """
        self.id = id
        self.context = context
        self.name = name
        self.resource_type = resource_type
        self.data = data
        self.created_on = created_on
        self.deleted = deleted
        self.deleted_on = deleted_on

    @property
    def url(self) -> str:
        """
        Return the content URL.
        """
        return f'/{self.context}/{self.resource_type}/{self.name}'

    def to_dict(self) -> dict[str, Any]:
        """
        Parse object to dict.
        """
        return dict(
            id=self.id,
            context=self.context,
            name=self.name,
            resource_type=self.resource_type,
            data=self.data,
            created_on=self.created_on,
            deleted=self.deleted,
            deleted_on=self.deleted_on
        )

    @classmethod
    def map_dict_to_entity(cls, dct: dict[str, Any]) -> 'ContentEntity':
        """
        Map dict to content.
        """
        return ContentEntity(
            id=dct.get('id', -1),
            context=dct.get('context', None),
            name=dct.get('name', None),
            resource_type=dct.get('resource_type', None),
            data=json.loads(dct.get('data', None)),
            created_on=dct.get('created_on', None),
            deleted=str(dct.get('deleted')) == '1',
            deleted_on=dct.get('deleted_on'),
        )

    @classmethod
    def map_list_to_entity(cls, lst: list[dict[str, Any]]
                           ) -> list['ContentEntity']:
        """
        Map list of dics to entity.
        """
        result = []
        for item in lst:
            result.append(cls.map_dict_to_entity(item))
        return result
