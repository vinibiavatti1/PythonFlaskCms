"""
Object repository.
"""
from typing import Any, Optional

from project.utils import database_utils
from project.entities.object_entity import ObjectEntity


TABLE_NAME = 'objects'


def select_by_type(context: str, object_type: str) -> list[ObjectEntity]:
    """
    Select objects by type.
    """
    sql = f'''
        SELECT * FROM {TABLE_NAME}
        WHERE context = ? AND object_type = ? AND deleted = 0
        ORDER BY object_order
    '''
    parameters = (context, object_type,)
    result_set = database_utils.execute_query(sql, parameters)
    return ObjectEntity.map_list_to_entity(result_set)


def select_next_order_by_reference(context: str, reference_name: str) -> int:
    """
    Select next order by reference.
    """
    sql = f'''
        SELECT MAX(object_order) + 1 as `result` FROM {TABLE_NAME}
        WHERE reference_name = ? AND context = ?
    '''
    parameters = (reference_name, context)
    result_set = database_utils.execute_single_query(sql, parameters)
    if result_set is None or result_set['result'] is None:
        return 1
    return int(result_set['result'])


def select_next_root_order(context: str) -> int:
    """
    Select next root order.
    """
    sql = f'''
        SELECT MAX(object_order) + 1 as `result` FROM {TABLE_NAME}
        WHERE reference_name IS NULL AND context = ?
    '''
    parameters = (context,)
    result_set = database_utils.execute_single_query(sql, parameters)
    if result_set is None or result_set['result'] is None:
        return 1
    return int(result_set['result'])


def select_deleted_by_type(context: str, object_type: str
                           ) -> list[ObjectEntity]:
    """
    Select deleted objects by type.
    """
    sql = f'''
        SELECT * FROM {TABLE_NAME}
        WHERE context = ? AND object_type = ? AND deleted = 1
        ORDER BY object_order
    '''
    parameters = (context, object_type,)
    result_set = database_utils.execute_query(sql, parameters)
    return ObjectEntity.map_list_to_entity(result_set)


def select_all_deleted(context: str) -> list[ObjectEntity]:
    """
    Select all deleted objects.
    """
    sql = f'''
        SELECT * FROM {TABLE_NAME}
        WHERE context = ? AND deleted = 1
        ORDER BY object_order
    '''
    parameters = (context,)
    result_set = database_utils.execute_query(sql, parameters)
    return ObjectEntity.map_list_to_entity(result_set)


def select_all(context: str) -> list[ObjectEntity]:
    """
    Select all objects.
    """
    sql = f'''
        SELECT * FROM {TABLE_NAME}
        WHERE context = ? AND deleted = 0
        ORDER BY reference_name
    '''
    parameters = (context,)
    result_set = database_utils.execute_query(sql, parameters)
    return ObjectEntity.map_list_to_entity(result_set)


def select_by_reference(context: str, reference_name: str
                        ) -> list[ObjectEntity]:
    """
    Select objects by reference.
    """
    sql = f'''
        SELECT * FROM {TABLE_NAME}
        WHERE reference_name = ? AND context = ? AND deleted = 0
        ORDER BY object_order
    '''
    parameters = (reference_name, context)
    result_set = database_utils.execute_query(sql, parameters)
    return ObjectEntity.map_list_to_entity(result_set)


def select_root_objects(context: str) -> list[ObjectEntity]:
    """
    Select roots objects.
    """
    sql = f'''
        SELECT * FROM {TABLE_NAME}
        WHERE reference_name is NULL AND context = ? AND deleted = 0
        ORDER BY object_order
    '''
    parameters = (context,)
    result_set = database_utils.execute_query(sql, parameters)
    return ObjectEntity.map_list_to_entity(result_set)


def select_by_id(object_id: int) -> Optional[ObjectEntity]:
    """
    Select objects by id.
    """
    sql = f'''
        SELECT * FROM {TABLE_NAME}
        WHERE id = ?
    '''
    parameters = (object_id,)
    result_set = database_utils.execute_single_query(sql, parameters)
    if not result_set:
        return None
    return ObjectEntity.map_dict_to_entity(result_set)


def select_by_name(context: str, name: str) -> Optional[ObjectEntity]:
    """
    Select object by name.
    """
    sql = f'''
        SELECT * FROM {TABLE_NAME}
        WHERE context = ? AND name = ? AND deleted = 0
    '''
    parameters = (context, name)
    result_set = database_utils.execute_single_query(sql, parameters)
    if result_set is None:
        return None
    return ObjectEntity.map_dict_to_entity(result_set)


def insert(entity: ObjectEntity) -> Any:
    """
    Insert a new object and return the generated id.
    """
    sql = f'''
        INSERT INTO {TABLE_NAME}
        (context, name, object_type, reference_name, object_order, properties)
        VALUES
        (?, ?, ?, ?, ?, ?)
    '''
    object_order = None
    if entity.reference_name is None:
        object_order = select_next_root_order(
            entity.context
        )
    else:
        object_order = select_next_order_by_reference(
            entity.context, entity.reference_name
        )
    parameters = (
        entity.context,
        entity.name,
        entity.object_type,
        entity.reference_name,
        object_order,
        entity.get_properties_as_json(),
    )
    entity_id = database_utils.execute_update(sql, parameters)
    return entity_id


def update(entity: ObjectEntity) -> Any:
    """
    Update an object and returin its id.
    """
    sql = f'''
        UPDATE {TABLE_NAME}
        SET context = ?, name = ?, object_type = ?, properties = ?
        WHERE id = ?
    '''
    parameters = (
        entity.context,
        entity.name,
        entity.object_type,
        entity.get_properties_as_json(),
        entity.id,
    )
    database_utils.execute_update(sql, parameters)
    return entity.id


def update_order(object_id: int, object_order: int) -> Any:
    """
    Update object order by id.
    """
    sql = f'''
        UPDATE {TABLE_NAME}
        SET object_order = ?
        WHERE id = ?
    '''
    parameters = (
        object_order,
        object_id,
    )
    database_utils.execute_update(sql, parameters)
    return object_id


def delete(object_id: int) -> Any:
    """
    Delete an object and return its id.
    """
    sql = f'''
        UPDATE {TABLE_NAME}
        SET deleted = 1, deleted_on = CURRENT_TIMESTAMP
        WHERE id = ?
    '''
    parameters = (object_id,)
    database_utils.execute_update(sql, parameters)
    return object_id


def restore(object_id: int) -> Any:
    """
    Restore a deleted object and return its id.
    """
    sql = f'''
        UPDATE {TABLE_NAME}
        SET deleted = 0, deleted_on = NULL
        WHERE id = ?
    '''
    parameters = (object_id,)
    database_utils.execute_update(sql, parameters)
    return object_id
