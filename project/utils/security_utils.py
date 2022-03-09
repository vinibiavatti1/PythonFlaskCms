"""
Security utilities module.
"""
from flask import abort, request, redirect
from functools import wraps
from flask.helpers import flash
from project.enums import session_enum
from flask import session
from typing import Any, Callable
from hashlib import sha256
from project.enums import security_enum
from project.services.user_service import is_user_active
from project.services.auth_service import do_logout


###############################################################################
# Decorators
###############################################################################


def login_required(*, methods: list[str] = [],
                   permissions: list[int] = []) -> Callable[[Any], Any]:
    """
    Route login required decorator.

    Validates user session before process the resource. Can be used to decorate
    route functions to set the route only if the user is authenticated. Set
    methods to block specific methods, otherwise, all methods will be blocked.
    """
    def decorator_wrapper(fn: Callable[[Any], Any]) -> Callable[[Any], Any]:
        @wraps(fn)
        def wrapper(*args: list[Any], **kwargs: dict[str, Any]) -> Any:
            if methods and request.method not in methods:
                return fn(*args, **kwargs)
            if not is_authenticated():
                return abort(401)
            if permissions and not has_permission(permissions):
                return abort(401)
            return fn(*args, **kwargs)
        return wrapper
    return decorator_wrapper


def validate_user_in_db() -> Callable[[Any], Any]:
    """
    Validates the user in database checking if user is active and not deleted.
    """
    def decorator_wrapper(fn: Callable[[Any], Any]) -> Callable[[Any], Any]:
        @wraps(fn)
        def wrapper(*args: list[Any], **kwargs: list[Any]) -> Any:
            if not is_user_active(session[session_enum.USER_ID]):
                do_logout()
                flash('Your session has been expired', category='error')
                return redirect('/login')
            return fn(*args, **kwargs)
        return wrapper
    return decorator_wrapper


###############################################################################
# Functions
###############################################################################


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
