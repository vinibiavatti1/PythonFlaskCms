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
            resource_id,
            description,
            created_by,
            resource_type
        ) VALUES (?, ?, ?, ?)
    '''
    return database_utils.execute_update(sql, (
        data['resource_id'],
        data['description'],
        data['created_by'],
        data['resource_type'],
    ))


def select_by_resource(resource_id: int, resource_type: str
                      ) -> list[dict[str, Any]]:
    """
    Get all history records by resource id.
    """
    sql = '''
        SELECT
            h.id,
            h.description,
            h.created_by,
            h.resource_type,
            u.name as created_by_name,
            h.created_on
        FROM history h
        LEFT JOIN users u
        ON (h.created_by = u.id)
        WHERE h.resource_id = ?
        AND h.resource_type = ?
        AND h.deleted = 0 ORDER BY h.id DESC'''
    return database_utils.execute_query(sql, (
        resource_id,
        resource_type,
    ))
