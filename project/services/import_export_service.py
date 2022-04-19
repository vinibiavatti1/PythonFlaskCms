"""
Import/Export service.
"""
from typing import Any
from project.entities.object_entity import ObjectEntity
from project.services import object_service
from project.services import property_service
from project.services import user_service
from project.enums import import_action_enum
import json


def export_objects_by_id_list(id_list: list[int]) -> list[dict[str, Any]]:
    """
    Export objects as list of dict.
    """
    objects: list[ObjectEntity] = list()
    for id_ in id_list:
        entity = object_service.select_by_id(id_)
        if entity is None:
            continue
        objects.append(entity)
    return [e.to_dict() for e in objects]


def export_properties_by_id_list(id_list: list[int]) -> list[dict[str, Any]]:
    """
    Export properties as list of dict.
    """
    properties: list[dict[str, Any]] = list()
    for id_ in id_list:
        property = property_service.select_by_id(id_)
        if property is None:
            continue
        properties.append(dict(property))
    return properties


def export_users() -> list[dict[str, Any]]:
    """
    Export users as list of dict.
    """
    data = user_service.select_all()
    return [dict(d) for d in data]


def export_files() -> Any:
    """
    Export files as zip file.
    """
    return None  # TODO


def import_objects(json_data: str, import_action: str) -> None:
    """
    Import json data to objects table.
    """
    data = json.loads(json_data)
    for item in data:
        item['properties'] = json.dumps(item['properties'])
    entities = ObjectEntity.map_list_to_entity(data)
    for entity in entities:
        existent = object_service.select_by_name(
            entity.context, entity.name,
        )

        if import_action == import_action_enum.KEEP_BOTH:
            exist = existent is not None
            initial_name = entity.name
            index = 0
            while exist:
                index += 1
                entity.name = initial_name + f'_{index}'
                exist = object_service.object_exists(
                    entity.context, entity.name,
                )
            object_service.insert(entity)
        elif import_action == import_action_enum.IGNORE:
            if existent is None:
                object_service.insert(entity)
        elif import_action == import_action_enum.REPLACE:
            if existent is not None:
                entity.id = existent.id
                object_service.update_entity(entity)
            else:
                object_service.insert(entity)
        else:
            raise ValueError(
                f'Invalid import action: {import_action}'
            )


def import_properties(json_data: str, import_action: str) -> None:
    """
    Import json data to objects table.
    """
    data = json.loads(json_data)
    for item in data:
        existent = object_service.select_by_name(
            item['context'], item['name'],
        )
        if existent is None or import_action == import_action_enum.REPLACE:
            property_service.set_property(
                item['context'],
                item['name'],
                item['value'],
            )
