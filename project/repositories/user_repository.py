"""
Page SQLite repository.
"""
from typing import Any, Optional
from project.utils import database_utils


def select_by_email_and_password(email: str, password_hash: str) -> list[Any]:
    """
    Validate user by email and password pages.
    """
    sql = '''
        SELECT * FROM users
        WHERE email = ?
        AND password = ?
        AND active = 1
        AND deleted = 0
    '''
    return database_utils.execute_query(sql, (email, password_hash))


def select(id_user: int) -> Optional[Any]:
    """
    Return the user by id.
    """
    sql = '''
        SELECT * FROM users WHERE id = ? AND deleted = 0
    '''
    return database_utils.execute_single_query(sql, (id_user,))
