"""
History repository.
"""
from typing import Any
from project.utils import database_utils
from project.entities.history_entity import HistoryEntity


def insert(entity: HistoryEntity) -> Any:
    """
    Insert a new history and return its id.
    """
    sql = '''
        INSERT INTO history
        (context, table_name, target_id, description, created_by)
        VALUES (?, ?, ?, ?, ?)
    '''
    return database_utils.execute_update(sql, (
        entity.context,
        entity.table_name,
        entity.target_id,
        entity.description,
        entity.created_by
    ))


def select_by_target_id(context: str, table_name: str, target_id: int
                        ) -> list[HistoryEntity]:
    """
    Select history records by target id from table.
    """
    sql = '''
        SELECT
            history.id,
            history.context,
            history.description,
            history.table_name,
            history.created_by,
            history.created_on,
            users.name as user_name
        FROM history
        LEFT JOIN users
        ON history.created_by = users.id
        WHERE context = ? AND
              history.table_name = ? AND
              history.target_id = ?
        AND history.resource_type = ?
        AND history.deleted = 0 ORDER BY h.id DESC'''
    parameters = (context, table_name, target_id)
    result_set = database_utils.execute_query(sql, parameters)
    return HistoryEntity.map_list_to_entity(result_set)
