"""
Property functions module.
"""
from flask import session
from typing import Any, Optional
from project.enums import session_enum
from project.repositories import property_repository
from project.records.property_records import property_records


def set_properties(properties: dict[str, Any]) -> None:
    """
    Set properties value into database.
    """
    context = session[session_enum.CONTEXT]
    for name, value in properties.items():
        property_repository.set_property(context, name, value)


def set_property(name: str, value: Any) -> None:
    """
    Set property value into database.
    """
    context = session[session_enum.CONTEXT]
    property_repository.set_property(context, name, value)


def property_exists(name: str) -> bool:
    """
    Return True if the property is set in database.
    """
    context = session[session_enum.CONTEXT]
    property_value = property_repository.get_property(context, name)
    return property_value is not None


def get_property(name: str) -> str:
    """
    Get property value from database.
    """
    context = session[session_enum.CONTEXT]
    value = property_repository.get_property(context, name)
    if value is None:
        return ''
    return value


def select_all() -> dict[str, str]:
    """
    Get all properties from database.
    """
    context = session[session_enum.CONTEXT]
    properties = property_repository.select_all(context)
    result = dict()
    for prop in properties:
        result[prop['name']] = prop['value']
    return result
