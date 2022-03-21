"""
Context utilities.
"""
from flask import g
from project.records.context_records import context_records


def get_current_context() -> str:
    """
    Get the current context from flask global variable.
    """
    if not g.context:
        for context_record in context_records:
            if context_record.default:
                return context_record.code
        return ''
    return str(g.context)


def set_current_context(context: str) -> None:
    """
    Set the current context to flask global variable.
    """
    g.context = context
