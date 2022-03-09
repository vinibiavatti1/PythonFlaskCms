"""
Property functions module.
"""
from typing import Any
from project.repositories import property_repository
from project.registry.properties import properties


def set_properties(properties: dict[str, Any]) -> None:
    """
    Set properties value into database.
    """
    for name, value in properties.items():
        property_repository.set_property(name, value)


def set_property(name: str, value: Any) -> None:
    """
    Set property value into database.
    """
    property_repository.set_property(name, value)


def property_exists(name: str) -> bool:
    """
    Return True if the property is set in database.
    """
    property_value = property_repository.get_property(name)
    return property_value is not None


def get_property(name: str) -> Any:
    """
    Get property value from database.
    """
    return property_repository.get_property(name)


def select_all() -> dict[str, Any]:
    """
    Get all properties from database.
    """
    properties = property_repository.select_all()
    result = dict()
    for prop in properties:
        result[prop['name']] = prop['value']
    return result
