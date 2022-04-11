"""
Object repository.
"""
from typing import Any, Optional
from project.utils import database_utils
from project.entities.object_entity import ObjectEntity


TABLE_NAME = 'objects'


def select_by_type_and_subtype(context: str, object_type: str,
                               object_subtype: str) -> list[ObjectEntity]:
    """
    Select objects by type and subtype.
    """
    sql = f'''
        SELECT * FROM {TABLE_NAME}
        WHERE context = ? AND object_type = ? AND object_subtype = ? AND
              deleted = 0
    '''
    parameters = (context, object_type, object_subtype,)
    result_set = database_utils.execute_query(sql, parameters)
    return ObjectEntity.map_list_to_entity(result_set)


def select_by_type(context: str, object_type: str) -> list[ObjectEntity]:
    """
    Select objects by type.
    """
    sql = f'''
        SELECT * FROM {TABLE_NAME}
        WHERE context = ? AND object_type = ? AND deleted = 0
    '''
    parameters = (context, object_type,)
    result_set = database_utils.execute_query(sql, parameters)
    return ObjectEntity.map_list_to_entity(result_set)


def select_deleted_by_type(context: str, object_type: str
                           ) -> list[ObjectEntity]:
    """
    Select deleted objects by type.
    """
    sql = f'''
        SELECT * FROM {TABLE_NAME}
        WHERE context = ? AND object_type = ? AND deleted = 1
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


def select_by_name(context: str, object_type: str, object_subtype: str,
                   name: str) -> Optional[ObjectEntity]:
    """
    Select objects by name.
    """
    sql = f'''
        SELECT * FROM {TABLE_NAME}
        WHERE context = ? AND object_type = ? AND object_subtype = ? AND
              name = ? AND deleted = 0
    '''
    parameters = (context, object_type, object_subtype, name,)
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
        (context, name, object_type, object_subtype, properties)
        VALUES
        (?, ?, ?, ?, ?)
    '''
    parameters = (
        entity.context,
        entity.name,
        entity.object_type,
        entity.object_subtype,
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
        SET context = ?, name = ?, object_type = ?, object_subtype = ?,
            properties = ?
        WHERE id = ?
    '''
    parameters = (
        entity.context,
        entity.name,
        entity.object_type,
        entity.object_subtype,
        entity.get_properties_as_json(),
        entity.id,
    )
    database_utils.execute_update(sql, parameters)
    return entity.id


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
