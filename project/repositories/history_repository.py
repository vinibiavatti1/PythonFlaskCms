"""
History repository.
"""
from typing import Any, Optional
from project.utils import database_utils


def insert(data: dict[str, Any]) -> Any:
    """
    Insert history.
    """
    sql = '''
        INSERT INTO history (
            type_resource,
            id_resource,
            description,
            created_by
        ) VALUES (?, ?, ?, ?)
    '''
    return database_utils.execute_update(sql, (
        data['type_resource'],
        data['id_resource'],
        data['description'],
        data['created_by'],
    ))


def select_by_resource(resource_id: int,
                       resource_type: str) -> list[dict[str, Any]]:
    """
    Get all history records by resource id.
    """
    sql = '''
        SELECT
            h.id,
            h.description,
            h.created_by,
            u.name as created_by_name,
            h.created_on
        FROM history h
        LEFT JOIN users u
        ON (h.created_by = u.id)
        WHERE h.id_resource = ?
        AND h.type_resource = ?
        AND h.deleted = 0 ORDER BY h.id DESC'''
    return database_utils.execute_query(sql, (resource_id, resource_type))
