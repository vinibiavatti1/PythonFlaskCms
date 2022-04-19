"""
Property repository.
"""
from typing import Any, Optional
from project.utils import database_utils


def delete_property(context: str, name: str) -> None:
    """
    Delete property by name.
    """
    sql = 'DELETE FROM properties WHERE name = ? AND context = ?'
    database_utils.execute_update(sql, (name, context))


def select_all(context: str) -> list[dict[str, str]]:
    """
    Get all properties.
    """
    sql = 'SELECT * FROM properties WHERE context = ?'
    return database_utils.execute_query(sql, (context,))


def select_by_id(id_property: int) -> Optional[dict[str, Any]]:
    """
    Get property by id.
    """
    sql = 'SELECT * FROM properties WHERE id = ?'
    return database_utils.execute_single_query(sql, (id_property,))


def set_property(context: str, name: str, value: str) -> None:
    """
    Set property value.
    """
    delete_property(context, name)
    sql = '''
        INSERT INTO properties
        (context, name, value)
        VALUES
        (?, ?, ?)
    '''
    database_utils.execute_update(sql, (context, name, value))


def get_property(context: str, name: str) -> Optional[dict[str, Any]]:
    """
    Get property value by name.
    """
    sql = 'SELECT * FROM properties WHERE name = ? AND context = ?'
    return database_utils.execute_single_query(sql, (name, context))
