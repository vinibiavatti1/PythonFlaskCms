"""
Object service.
"""
from typing import Any, Optional
from project.errors import EntityError
from project.models.builtin_object_model import BuiltinObjectModel
from project.models.object_model import ObjectModel
from project.repositories import object_repository
from project.services import history_service
from project.entities.object_entity import ObjectEntity
from project.enums import history_messages_enum
from project.enums import table_enum
from project.records.object_records import object_records
from copy import deepcopy


def select_by_type(context: str, object_type: str) -> list[ObjectEntity]:
    """
    Select objects by type.
    """
    return object_repository.select_by_type(context, object_type)


def select_by_reference(context: str, reference_name: str
                        ) -> list[ObjectEntity]:
    """
    Select objects by reference.
    """
    return object_repository.select_by_reference(context, reference_name)


def select_root_objects(context: str) -> list[ObjectEntity]:
    """
    Select root objects.
    """
    return object_repository.select_root_objects(context)


def select_deleted_by_type(context: str, object_type: str
                           ) -> list[ObjectEntity]:
    """
    Select deleted objects by type.
    """
    return object_repository.select_deleted_by_type(context, object_type)


def select_all_deleted(context: str) -> list[ObjectEntity]:
    """
    Select all deleted objects.
    """
    return object_repository.select_all_deleted(context)


def select_all(context: str) -> list[ObjectEntity]:
    """
    Select all objects.
    """
    return object_repository.select_all(context)


def select_by_id(object_id: int) -> Optional[ObjectEntity]:
    """
    Select objects by id.
    """
    return object_repository.select_by_id(object_id)


def object_exists(context: str, name: str) -> bool:
    """
    Return True if the object exist.
    """
    return object_repository.select_by_name(
        context, name
    ) is not None


def select_by_name(context: str, name: str) -> Optional[ObjectEntity]:
    """
    Select object by name.
    """
    return object_repository.select_by_name(
        context, name
    )


def insert(entity: ObjectEntity) -> Any:
    """
    Insert a new object and return the generated id.
    """
    if select_by_name(entity.context, entity.name) is not None:
        raise EntityError(f'The name "{entity.name}" already exists')
    entity_id = object_repository.insert(entity)
    history_service.insert(
        entity.context,
        table_enum.OBJECTS,
        entity_id,
        history_messages_enum.OBJECT_CREATED
    )
    return entity_id


def insert_builtin(context: str, builtin_object: BuiltinObjectModel) -> Any:
    """
    Insert a builtin object and return the generated id.
    """
    entity = ObjectEntity(
        context=context,
        name=builtin_object.name,
        object_type=builtin_object.object_type,
        properties=builtin_object.properties,
        reference_name=builtin_object.reference_name,
    )
    if select_by_name(entity.context, entity.name) is not None:
        raise EntityError(f'The name "{entity.name}" already exists')
    entity_id = object_repository.insert(entity)
    history_service.insert(
        entity.context,
        table_enum.OBJECTS,
        entity_id,
        history_messages_enum.OBJECT_CREATED
    )
    return entity_id


def update(object_id: int, properties: dict[str, Any]) -> Any:
    """
    Update entity with new data.
    """
    entity = select_by_id(object_id)
    if entity is None:
        raise EntityError(f'Entity not found: {object_id}')
    entity.name = properties['name']
    entity.properties = properties
    return update_entity(entity)


def update_entity(entity: ObjectEntity) -> Any:
    """
    Update an object and returin its id.
    """
    found = select_by_name(entity.context, entity.name)
    if found is not None and found.id != entity.id:
        raise EntityError(f'The name "{entity.name}" already exists')
    entity_id = object_repository.update(entity)
    history_service.insert(
        entity.context,
        table_enum.OBJECTS,
        entity_id,
        history_messages_enum.OBJECT_UPDATED
    )
    return entity_id


def update_order(object_id: int, object_order: int) -> None:
    """
    Update object order by id.
    """
    object_repository.update_order(object_id, object_order)


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


def get_record_by_name(name: str) -> Optional[ObjectModel]:
    """
    Get object record by name.
    """
    for record in object_records:
        if record.name == name:
            return record
    return None


def get_records_by_names(names: list[str]) -> list[ObjectModel]:
    """
    Get objects by list of names.
    """
    records = []
    for name in names:
        record = get_record_by_name(name)
        if record:
            records.append(record)
    return records


def get_root_records() -> list[ObjectModel]:
    """
    Get root records.
    """
    result = []
    for record in object_records:
        if record.is_root:
            result.append(record)
    return result
