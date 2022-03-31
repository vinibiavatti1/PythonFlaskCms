"""
Object service.
"""
from typing import Any, Optional
from project.repositories import object_repository
from project.services import history_service
from project.entities.object_entity import ObjectEntity
from project.enums import history_messages_enum
from project.enums import table_enum
from copy import deepcopy


def select_by_type_and_subtype(context: str, object_type: str,
                               object_subtype: str) -> list[ObjectEntity]:
    """
    Select objects by type and subtype.
    """
    return object_repository.select_by_type_and_subtype(
        context, object_type, object_subtype
    )


def select_by_type(context: str, object_type: str) -> list[ObjectEntity]:
    """
    Select objects by type.
    """
    return object_repository.select_by_type(context, object_type)


def select_deleted_by_type(context: str, object_type: str
                           ) -> list[ObjectEntity]:
    """
    Select deleted objects by type.
    """
    return object_repository.select_deleted_by_type(context, object_type)


def select_by_id(object_id: int) -> Optional[ObjectEntity]:
    """
    Select objects by id.
    """
    return object_repository.select_by_id(object_id)


def select_by_name(context: str, object_type: str, object_subtype: str,
                   name: str) -> Optional[ObjectEntity]:
    """
    Select objects by name.
    """
    return object_repository.select_by_name(
        context, object_type, object_subtype, name
    )


def insert(entity: ObjectEntity) -> Any:
    """
    Insert a new object and return the generated id.
    """
    entity_id = object_repository.insert(entity)
    history_service.insert(
        entity.context,
        table_enum.OBJECTS,
        entity_id,
        history_messages_enum.OBJECT_CREATED
    )
    return entity_id


def update(entity: ObjectEntity) -> Any:
    """
    Update an object and returin its id.
    """
    entity_id = object_repository.update(entity)
    history_service.insert(
        entity.context,
        table_enum.OBJECTS,
        entity_id,
        history_messages_enum.OBJECT_UPDATED
    )
    return entity_id


def delete(object_id: int) -> Any:
    """
    Delete an object and return its id.
    """
    entity = object_repository.select_by_id(object_id)
    if entity is None:
        return
    object_repository.delete(object_id)
    history_service.insert(
        entity.context,
        table_enum.OBJECTS,
        object_id,
        history_messages_enum.OBJECT_DELETED
    )
    return object_id


def restore(object_id: int) -> Any:
    """
    Restore a deleted object and return its id.
    """
    entity = object_repository.select_by_id(object_id)
    if entity is None:
        return
    object_repository.restore(object_id)
    history_service.insert(
        entity.context,
        table_enum.OBJECTS,
        object_id,
        history_messages_enum.OBJECT_RESTORED
    )
    return object_id


def duplicate(object_id: int, to_context: str, new_name: str) -> Any:
    """
    Duplicate an existent object and return its id.
    """
    entity = object_repository.select_by_id(object_id)
    if not entity:
        return None
    new_object = deepcopy(entity)
    new_object.name = new_name
    new_object.context = to_context
    new_id = object_repository.insert(new_object)
    history_service.insert(
        entity.context,
        table_enum.OBJECTS,
        entity.id,
        history_messages_enum.OBJECT_DUPLICATED_TO.format(
            to_context,
            new_id,
        ),
    )
    history_service.insert(
        to_context,
        table_enum.OBJECTS,
        new_id,
        history_messages_enum.OBJECT_DUPLICATED_FROM.format(
            entity.context,
            entity.id,
        ),
    )
    return new_id
