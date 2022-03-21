"""
Context decorators.
"""
from flask import abort, g
from typing import Any, Callable
from project.records.context_records import context_records
from functools import wraps


def process_context() -> Callable[[Any], Any]:
    """
    Validate context decorator.
    """
    def decorator_wrapper(fn: Callable[[Any], Any]) -> Callable[[Any], Any]:
        @wraps(fn)
        def wrapper(*args: list[Any], **kwargs: Any) -> Any:
            context = kwargs.get('context')
            for context_record in context_records:
                if context_record.code == context:
                    g.context = context_record.code
                    return fn(*args, **kwargs)
            return abort(404)
        return wrapper
    return decorator_wrapper
