"""
Property functions module.
"""
from flask import session
from typing import Any
from project.enums import session_enum
from project.repositories import property_repository


def set_properties(context: str, properties: dict[str, Any]) -> None:
    """
    Set properties value into database.
    """
    for name, value in properties.items():
        property_repository.set_property(context, name, value)


def set_property(context: str, name: str, value: Any) -> None:
    """
    Set property value into database.
    """
    property_repository.set_property(context, name, value)


def property_exists(context: str, name: str) -> bool:
    """
    Return True if the property is set in database.
    """
    property_value = property_repository.get_property(context, name)
    return property_value is not None


def get_property(context: str, name: str) -> str:
    """
    Get property value from database.
    """
    value = property_repository.get_property(context, name)
    if value is None:
        return ''
    return value


def select_all(context: str) -> dict[str, str]:
    """
    Get all properties from database.
    """
    properties = property_repository.select_all(context)
    result = dict()
    for prop in properties:
        result[prop['name']] = prop['value']
    return result
