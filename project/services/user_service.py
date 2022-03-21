"""
User service.

This module provides business rule functions for user.
"""
from typing import Any, Optional
from project.repositories import user_repository
from project.utils import security_utils


def login(email: str, password: str) -> bool:
    """
    Do login by email and password.
    """
    password = security_utils.generate_hash(password)
    user = user_repository.select_by_email_and_password(email, password)
    return user is not None


def is_user_active(user_id: int) -> bool:
    """
    Return True if the user is active and not deleted, otherwise False.
    """
    user = user_repository.select(user_id)
    return user is not None


def select_by_email(email: str) -> Optional[dict[str, Any]]:
    """
    Select user by email.
    """
    return user_repository.select_by_email(email)


def insert(data: dict[str, Any]) -> Any:
    """
    Insert user to database.
    """
    data['password'] = security_utils.generate_hash(data['password'])
    return user_repository.insert(data)
