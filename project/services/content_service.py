"""
Content service.
"""
from typing import Any, Optional
from project.repositories import content_repository
from project.services import history_service
from project.entities.content_entity import ContentEntity
from project.enums import history_messages_enum
from copy import deepcopy


def select_all_by_type(context: str, resource_type: str
                       ) -> list[ContentEntity]:
    """
    Select all contents by content type.
    """
    return content_repository.select_all_by_type(context, resource_type)


def select_all_deleted(context: str) -> list[ContentEntity]:
    """
    Select all deleted contents.
    """
    return content_repository.select_all_deleted(context)


def select_all_published(context: str) -> list[ContentEntity]:
    """
    Select all published content.
    """
    contents = content_repository.select_all(context)
    return [c for c in contents if c.data['published'] == '1']


def select_by_id(content_id: int) -> Optional[ContentEntity]:
    """
    Select a content by id.
    """
    return content_repository.select_by_id(content_id)


def insert(resource: ContentEntity) -> Any:
    """
    Insert a new content.
    """
    content_id = content_repository.insert(resource)
    history_service.insert(
        content_id,
        resource.resource_type,
        history_messages_enum.RESOURCE_CREATED,
    )
    return content_id


def update(resource: ContentEntity) -> Any:
    """
    Update a content.
    """
    content_id = content_repository.update(resource)
    history_service.insert(
        content_id,
        resource.resource_type,
        history_messages_enum.RESOURCE_UPDATED,
    )
    return content_id


def delete(content_id: int) -> Any:
    """
    Delete a content by id.
    """
    resource = content_repository.select_by_id(content_id)
    if not resource:
        return
    content_repository.delete(content_id)
    history_service.insert(
        content_id,
        resource.resource_type,
        history_messages_enum.RESOURCE_DELETED,
    )
    return content_id


def restore(content_id: int) -> Any:
    """
    Restore a content by id.
    """
    content_repository.restore(content_id)
    content = content_repository.select_by_id(content_id)
    if not content:
        return
    history_service.insert(
        content_id,
        content.resource_type,
        history_messages_enum.RESOURCE_RESTORED,
    )


def duplicate(content_id: int, to_context: str, new_name: str
              ) -> Optional[Any]:
    """
    Duplicate content by id.
    """
    content = content_repository.select_by_id(content_id)
    if not content:
        return None
    new_content = deepcopy(content)
    new_content.name = new_name
    new_content.context = to_context
    new_content.data['published'] = 0
    new_id = content_repository.insert(new_content)
    history_service.insert(
        new_id,
        new_content.resource_type,
        history_messages_enum.RESOURCE_DUPLICATED_FROM.format(content.id),
    )
    history_service.insert(
        content.id,
        new_content.resource_type,
        history_messages_enum.RESOURCE_DUPLICATED_TO.format(new_id),
    )
    return new_id
