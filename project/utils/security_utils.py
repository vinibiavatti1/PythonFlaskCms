"""
Security utilities module.
"""
from project.enums import session_enum
from flask import session
from hashlib import sha256
from project.enums import security_enum


def is_authenticated() -> bool:
    """
    Return true if the user is authenticated in the application.
    """
    return (session_enum.USER_ID in session and
            len(str(session[session_enum.USER_ID])) > 0)


def has_permission(*permissions: list[int]) -> bool:
    """
    Check if authenticated user has permission.
    """
    user_permission = session.get(session_enum.USER_PERMISSION, None)
    if not user_permission:
        return False
    return user_permission in permissions


def generate_hash(data: str) -> str:
    """
    Generate hash by data using config salt and SHA256.
    """
    result: str = data + security_enum.SALT
    return sha256(result.encode()).hexdigest()
