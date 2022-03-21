"""
Context decorators.
"""
from flask import abort
from typing import Any, Callable
from project.records.context_records import context_records
from project.utils import context_utils
from functools import wraps


def process_context() -> Callable[[Any], Any]:
    """
    Validate context decorator.
    """
    def decorator_wrapper(fn: Callable[[Any], Any]) -> Callable[[Any], Any]:
        @wraps(fn)
        def wrapper(*args: list[Any], **kwargs: Any) -> Any:
            context = kwargs.get('context')
            if context is None:
                return abort(400)
            for context_record in context_records:
                if context_record.code == context:
                    context_utils.set_current_context(context_record.code)
                    return fn(*args, **kwargs)
            return abort(404)
        return wrapper
    return decorator_wrapper
