"""
History entity.

Model to map database history entity.
"""
from flask import request, session, current_app, has_request_context
from project.enums import session_enum
from typing import Any, Optional
from datetime import datetime


class HistoryEntity:
    """
    History entity class.
    """

    def __init__(self, *,
                 id: int = -1,
                 context: str,
                 table_name: str,
                 target_id: int,
                 description: str,
                 created_by: Optional[int] = None,
                 created_on: datetime = datetime.now(),
                 ) -> None:
        """
        Init history entity object.
        """
        self.id = id
        self.context = context
        self.table_name = table_name
        self.target_id = target_id
        self.description = description
        self.created_on = created_on
        self.created_by = created_by
        if has_request_context() and self.created_by is None:
            self.created_by = session.get(session_enum.USER_ID, None)

    @classmethod
    def map_dict_to_entity(cls, dct: dict[str, Any]) -> 'HistoryEntity':
        """
        Map dict to content.
        """
        dct = dict(dct)
        return HistoryEntity(
            id=dct.get('id', -1),
            context=dct.get('context', None),
            table_name=dct.get('table_name', None),
            target_id=dct.get('target_id', None),
            description=dct.get('description', None),
            created_on=dct.get('created_on', None),
            created_by=dct.get('created_by', None),
        )

    @classmethod
    def map_list_to_entity(cls, lst: list[dict[str, Any]]
                           ) -> list['HistoryEntity']:
        """
        Map list of dics to entity.
        """
        result = []
        for item in lst:
            result.append(cls.map_dict_to_entity(item))
        return result
