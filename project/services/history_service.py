"""
History functions module.
"""
from flask import session
from project.enums import session_enum
from typing import Any
from project.repositories import history_repository
from project.records.properties import properties


def insert(resource_id: int, type_resource: str, description: str) -> None:
    """
    Insert new history.
    """
    user_id = session[session_enum.USER_ID]
    data = dict(
        id_resource=resource_id,
        type_resource=type_resource,
        description=description,
        created_by=user_id
    )
    history_repository.insert(data)


def select_by_resource_id(resource_id: int) -> list[dict[str, Any]]:
    """
    Select the history by resource id.
    """
    return history_repository.select_by_resource_id(resource_id)