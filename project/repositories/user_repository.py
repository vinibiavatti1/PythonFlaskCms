"""
Page SQLite repository.
"""
from typing import Any, Optional
from project.utils import database_utils


def select_by_email_and_password(email: str, password_hash: str
                                 ) -> Optional[dict[str, Any]]:
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
    return database_utils.execute_single_query(sql, (email, password_hash))


def select_by_email(email: str) -> Optional[dict[str, Any]]:
    """
    Select user by email.
    """
    sql = '''
        SELECT * FROM users
        WHERE email = ?
        AND deleted = 0
    '''
    return database_utils.execute_single_query(sql, (email,))


def select(id_user: int) -> Optional[Any]:
    """
    Return the user by id.
    """
    sql = '''
        SELECT * FROM users WHERE id = ? AND deleted = 0
    '''
    return database_utils.execute_single_query(sql, (id_user,))


def select_all() -> list[dict[str, Any]]:
    """
    Return all users.
    """
    sql = '''
        SELECT * FROM users WHERE deleted = 0
    '''
    return database_utils.execute_query(sql)


def insert(data: dict[str, Any]) -> Any:
    """
    Add a new user.
    """
    sql = '''
        INSERT INTO users (name, email, password, permission)
        VALUES (?, ?, ?, ?)
    '''
    return database_utils.execute_update(sql, (
        data['name'],
        data['email'],
        data['password'],
        data['permission'],
    ))


def update_last_login(user_id: int) -> None:
    """
    Update user last login date by user id.
    """
    sql = '''
        UPDATE users SET last_login = CURRENT_TIMESTAMP
        WHERE id = ?
    '''
    database_utils.execute_update(sql, (user_id,))
