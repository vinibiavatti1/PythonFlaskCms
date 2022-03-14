"""
Translation repository.
"""
from typing import Any, Optional
from project.utils import database_utils


def insert(data: dict[str, Any]) -> Any:
    """
    Insert translation.
    """
    sql = '''
        INSERT INTO translations (
            idiom,
            name,
            value
        ) VALUES (?, ?, ?)
    '''
    return database_utils.execute_update(sql, (
        data['idiom'],
        data['name'],
        data['value'],
    ))


def update(translation_id: int, data: dict[str, Any]) -> Any:
    """
    Update translation.
    """
    sql = '''
        UPDATE translations SET
            name = ?,
            value = ?,
            idiom = ?
        WHERE
            id = ?
    '''
    return database_utils.execute_update(sql, (
        data['idiom'],
        data['name'],
        data['value'],
        translation_id,
    ))


def select_all() -> list[dict[str, Any]]:
    """
    Get all translations records.
    """
    sql = '''
        SELECT * FROM translations
        WHERE deleted = 0 ORDER BY idiom
    '''
    return database_utils.execute_query(sql)


def select_by_id(translation_id: int) -> Optional[dict[str, Any]]:
    """
    Get translation by id.
    """
    sql = '''
        SELECT * FROM translations
        WHERE id = ? AND deleted = 0
    '''
    return database_utils.execute_single_query(sql, (translation_id,))


def delete(id_translation: int) -> list[dict[str, Any]]:
    """
    Delete translation.
    """
    sql = '''
        UPDATE translations SET deleted = 1
        WHERE id = ?
    '''
    return database_utils.execute_query(sql, (id_translation,))
