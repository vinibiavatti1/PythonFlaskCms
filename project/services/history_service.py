"""
History functions module.
"""
from flask import session, request
from project.enums import session_enum
from typing import Any
from project.repositories import history_repository


def insert(resource_id: int, resource_type: str, description: str) -> None:
    """
    Insert new history.
    """
    user_id = None
    if request:
        user_id = session[session_enum.USER_ID]
    data = dict(
        resource_type=resource_type,
        resource_id=resource_id,
        description=description,
        created_by=user_id
    )
    history_repository.insert(data)


def select_by_resource(resource_id: int, resource_type: str
                      ) -> list[dict[str, Any]]:
    """
    Select the history by resource id and type.
    """
    return history_repository.select_by_resource(resource_id, resource_type)
