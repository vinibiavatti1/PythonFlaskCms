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


def get_property(context: str, name: str) -> Optional[str]:
    """
    Get property value by name.
    """
    sql = 'SELECT * FROM properties WHERE name = ? AND context = ?'
    return database_utils.execute_single_query(sql, (name, context))
