"""
Property functions module.
"""
from flask import session
from typing import Any, Optional
from project.enums import session_enum
from project.models.header_model import HeaderModel
from project.models.property_model import PropertyModel
from project.repositories import property_repository
from project.records.property_records import property_records


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
    prop = property_repository.get_property(context, name)
    return prop is not None


def get_property_value(context: str, name: str, cast: type = str) -> Any:
    """
    Get property value from database.
    """
    prop = property_repository.get_property(context, name)
    if prop is None:
        return ''
    return cast(prop['value'])


def select_all_as_dict(context: str) -> dict[str, str]:
    """
    Get all properties from database.
    """
    properties = property_repository.select_all(context)
    result = dict()
    for prop in properties:
        result[prop['name']] = prop['value']
    return result


def select_all(context: str) -> list[dict[str, Any]]:
    """
    Get all properties as list from database.
    """
    return property_repository.select_all(context)


def select_by_id(id_property: int) -> Optional[dict[str, Any]]:
    """
    Get property by id.
    """
    return property_repository.select_by_id(id_property)


def get_record_by_name(name: str) -> Optional[PropertyModel]:
    """
    Get object record by name.
    """
    for record in property_records:
        if isinstance(record, HeaderModel):
            continue
        if record.name == name:
            return record
    return None
