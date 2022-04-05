"""
Controller utilities.
"""
from werkzeug import utils
from typing import Any

from project.models.property_model import PropertyModel


def escape_dict(data: dict[str, Any]) -> dict[str, Any]:
    """
    Escape all fields of dict.
    """
    return {k: utils.escape(v) for k, v in data.items()}


def escape(value: Any) -> str:
    """
    Alias to werkzeug::utils::escape.
    """
    return utils.escape(value)


def result_api_message(type: str, message: str) -> dict[str, Any]:
    """
    Generates a common dict response message with type and message.
    """
    return {
        'type': type,
        'message': message
    }


def get_object_root_url(context: str, object_type: str) -> str:
    """
    Get list url.
    """
    return f'/{context}/admin/objects/{object_type}'
