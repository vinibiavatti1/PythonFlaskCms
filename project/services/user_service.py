"""
User service.

This module provides business rule functions for user.
"""
from project.repositories import user_repository
from project.utils import security_utils


def login(email: str, password: str) -> bool:
    """
    Do login by email and password.
    """
    password = security_utils.generate_hash(password)
    users = user_repository.select_by_email_and_password(email, password)
    return len(users) == 1


def is_user_active(user_id: int) -> bool:
    """
    Return True if the user is active and not deleted, otherwise False.
    """
    user = user_repository.select(user_id)
    return user is not None
