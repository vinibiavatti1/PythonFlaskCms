"""
History service.
"""
from flask import session, request
from project.enums import session_enum
from typing import Any
from project.repositories import history_repository
from project.entities.history_entity import HistoryEntity


def insert_entity(entity: HistoryEntity) -> Any:
    """
    Insert new history by entity.
    """
    return history_repository.insert(entity)


def insert(context: str, table_name: str, target_id: int, description: str
           ) -> Any:
    """
    Insert new history.
    """
    entity = HistoryEntity(
        context=context,
        table_name=table_name,
        target_id=target_id,
        description=description,
    )
    return history_repository.insert(entity)


def select_by_target_id(context: str, table_name: str, target_id: int
                        ) -> list[HistoryEntity]:
    """
    Select the history by resource id and type.
    """
    return history_repository.select_by_target_id(
        context, table_name, target_id
    )
