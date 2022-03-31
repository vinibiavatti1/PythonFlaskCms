"""
Record decorators.
"""
from flask import abort
from typing import Any, Callable
from project.records.context_records import context_records
from project.utils import context_utils
from functools import wraps
from project.utils import record_utils


def validate_content_type() -> Callable[[Any], Any]:
    """
    Validate content type.
    """
    def decorator_wrapper(fn: Callable[[Any], Any]) -> Callable[[Any], Any]:
        @wraps(fn)
        def wrapper(*args: list[Any], **kwargs: Any) -> Any:
            content_type = kwargs.get('content_type', None)
            if content_type is None:
                return abort(400)
            content_record = record_utils.get_content_record(content_type)
            if content_record is None:
                return abort(404)
            return fn(*args, **kwargs)
        return wrapper
    return decorator_wrapper


def validate_resource_type() -> Callable[[Any], Any]:
    """
    Validate resource type.
    """
    def decorator_wrapper(fn: Callable[[Any], Any]) -> Callable[[Any], Any]:
        @wraps(fn)
        def wrapper(*args: list[Any], **kwargs: Any) -> Any:
            content_type = kwargs.get('resource_type', None)
            if content_type is None:
                return abort(400)
            content_record = record_utils.get_resource_record(content_type)
            if content_record is None:
                return abort(404)
            return fn(*args, **kwargs)
        return wrapper
    return decorator_wrapper


def validate_page_type() -> Callable[[Any], Any]:
    """
    Validate page type.
    """
    def decorator_wrapper(fn: Callable[[Any], Any]) -> Callable[[Any], Any]:
        @wraps(fn)
        def wrapper(*args: list[Any], **kwargs: Any) -> Any:
            content_type = kwargs.get('page_type', None)
            if content_type is None:
                return abort(400)
            content_record = record_utils.get_page_record(content_type)
            if content_record is None:
                return abort(404)
            return fn(*args, **kwargs)
        return wrapper
    return decorator_wrapper
