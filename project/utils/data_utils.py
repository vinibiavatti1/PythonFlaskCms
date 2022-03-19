"""
Data utilities.
"""
from typing import Any, Optional
from project.models.property_model import PropertyModel
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
                         content: dict[str, Any]) -> list[Any]:
    """
    Set properties value by name.
    """
    if 'data' not in content:
        return properties
    for prop in properties:
        if isinstance(prop, PropertyModel):
            prop.value = content['data'].get(prop.name, '')
    return properties
