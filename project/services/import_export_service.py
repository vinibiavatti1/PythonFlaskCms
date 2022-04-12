"""
Import/Export service.
"""
from typing import Any, Optional

from flask import current_app
from project.entities.object_entity import ObjectEntity
from project.services import object_service
from project.services import property_service
from project.services import user_service
from project.enums import import_action_enum
import json


def export_objects(context: str, object_type: Optional[str] = None,
                   object_subtype: Optional[str] = None
                   ) -> list[dict[str, Any]]:
    """
    Export objects as list of dict.
    """
    objects: list[ObjectEntity] = list()
    if object_type:
        objects = object_service.select_by_type(
            context, object_type
        )
    elif object_type and object_subtype:
        objects = object_service.select_by_type_and_subtype(
            context, object_type, object_subtype
        )
    else:
        objects = object_service.select_all(
            context
        )
    return [e.to_dict() for e in objects]


def export_component(context: str, component: str) -> list[dict[str, Any]]:
    """
    Export components as list of dict.
    """
    if component == 'navbar':
        return list()  # TODO
    elif component == 'footer':
        return list()  # TODO
    else:
        raise ValueError(f'Invalid component: {component}')


def export_properties(context: str) -> list[dict[str, Any]]:
    """
    Export properties as list of dict.
    """
    data = property_service.select_all_as_list(context)
    return [dict(d) for d in data]


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
            entity.context, entity.object_type, entity.object_subtype,
            entity.name,
        )

        if import_action == import_action_enum.KEEP_BOTH:
            exist = existent is not None
            initial_name = entity.name
            index = 0
            while exist:
                index += 1
                entity.name = initial_name + f'_{index}'
                exist = object_service.object_exists(
                    entity.context, entity.object_type, entity.object_subtype,
                    entity.name,
                )
            object_service.insert(entity)
        elif import_action == import_action_enum.IGNORE:
            if existent is None:
                object_service.insert(entity)
        elif import_action == import_action_enum.REPLACE:
            if existent is not None:
                entity.id = existent.id
                object_service.update(entity)
            else:
                object_service.insert(entity)
        else:
            raise ValueError(
                f'Invalid import action: {import_action}'
            )
