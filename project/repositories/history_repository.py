"""
History repository.
"""
from typing import Any, Optional
from project.utils import database_utils


def insert(context: str, data: dict[str, Any]) -> Any:
    """
    Insert history.
    """
    sql = '''
        INSERT INTO history (
            context,
            resource_type,
            resource_id,
            description,
            created_by
        ) VALUES (?, ?, ?, ?, ?)
    '''
    return database_utils.execute_update(sql, (
        context,
        data['resource_type'],
        data['resource_id'],
        data['description'],
        data['created_by'],
    ))


def select_by_resource(context: str, resource_id: int,
                       resource_type: str) -> list[dict[str, Any]]:
    """
    Get all history records by resource id.
    """
    sql = '''
        SELECT
            h.context,
            h.id,
            h.description,
            h.created_by,
            u.name as created_by_name,
            h.created_on
        FROM history h
        LEFT JOIN users u
        ON (h.created_by = u.id)
        WHERE h.resource_id = ?
        AND h.resource_type = ?
        AND h.deleted = 0 ORDER BY h.id DESC'''
    return database_utils.execute_query(sql, (
        resource_id, resource_type, context
    ))
