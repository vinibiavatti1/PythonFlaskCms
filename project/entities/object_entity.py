"""
Object entity.

Model to map database object entity.
"""
from typing import Any, Optional
from datetime import datetime
from project.enums import object_enum
import json


class ObjectEntity:
    """
    Object entity class.
    """

    ###########################################################################
    # Class Methods
    ###########################################################################

    @classmethod
    def map_dict_to_entity(cls, dct: dict[str, Any]) -> 'ObjectEntity':
        """
        Map dict to content.
        """
        dct = dict(dct)
        return ObjectEntity(
            id=dct.get('id', -1),
            context=dct.get('context', None),
            name=dct.get('name', None),
            object_type=dct.get('object_type', None),
            properties=json.loads(dct.get('properties', '{}')),
            created_on=dct.get('created_on', None),
            deleted=str(dct.get('deleted')) == '1',
            deleted_on=dct.get('deleted_on'),
            reference_name=dct.get('reference_name', None),
            object_order=dct.get('object_order', None),
        )

    @classmethod
    def map_list_to_entity(cls, lst: list[dict[str, Any]]
                           ) -> list['ObjectEntity']:
        """
        Map list of dics to entity.
        """
        result = []
        for item in lst:
            result.append(cls.map_dict_to_entity(item))
        return result

    ###########################################################################
    # Magic methods
    ###########################################################################

    def __init__(self, *,
                 id: int = -1,
                 context: str,
                 name: str,
                 object_type: str,
                 properties: dict[str, Any] = dict(),
                 created_on: datetime = datetime.now(),
                 deleted: bool = False,
                 deleted_on: Optional[datetime] = None,
                 reference_name: Optional[str] = None,
                 object_order: Optional[int] = None,
                 ) -> None:
        """
        Init object entity object.
        """
        self.id = id
        self.context = context
        self.name = name
        self.object_type = object_type
        self.properties = properties
        self.created_on = created_on
        self.deleted = deleted
        self.deleted_on = deleted_on
        self.reference_name = reference_name
        self.object_order = object_order

    ###########################################################################
    # Public Instance Methods
    ###########################################################################

    def to_dict(self) -> dict[str, Any]:
        """
        Parse object to dict.
        """
        return dict(
            id=self.id,
            context=self.context,
            name=self.name,
            object_type=self.object_type,
            properties=self.properties,
            created_on=self.created_on,
            deleted=self.deleted,
            deleted_on=self.deleted_on,
            reference_name=self.reference_name,
            object_order=self.object_order,
        )

    def get_properties_as_json(self) -> str:
        """
        Return properties as json string.
        """
        return json.dumps(self.properties)

    def set_properties_from_json(self, json_properties: str) -> None:
        """
        Set properties from json to dict.
        """
        self.properties = json.loads(json_properties)

    ###########################################################################
    # Properties
    ###########################################################################

    @property
    def url(self) -> str:
        """
        Return the content URL.
        """
        return f'/{self.context}/content/{self.name}'
