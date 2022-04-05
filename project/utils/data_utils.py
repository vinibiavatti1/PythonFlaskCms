"""
Data utilities.
"""
from typing import Any, Optional
from project.models.property_model import PropertyModel
from project.entities.object_entity import ObjectEntity
import json


def parse_json_data(data: dict[str, Any], json_field: str = 'data'
                    ) -> Optional[dict[str, Any]]:
    """
    Parse data transforming json str to json format.
    """
    if not data:
        return None
    result = {
        **data,
    }
    result[json_field] = json.loads(data[json_field])
    return result


def parse_list_json_data(data: list[dict[str, Any]], json_field: str = 'data'
                         ) -> list[dict[str, Any]]:
    """
    Parse list data transforming json str to json format for each element.
    """
    if not data or len(data) == 0:
        return list()
    results = []
    for element in data:
        result = parse_json_data(element, json_field)
        if not result:
            continue
        results.append(result)
    return results


def set_properties_value(properties: list[Any],
                         content: ObjectEntity) -> list[Any]:
    """
    Set properties value by name.
    """
    for prop in properties:
        if isinstance(prop, PropertyModel):
            if hasattr(content, prop.name):
                prop.value = getattr(content, prop.name)
            elif hasattr(content, 'properties'):
                prop.value = content.properties.get(prop.name, '')
    return properties
