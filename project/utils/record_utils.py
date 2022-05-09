"""
Record utilities.
"""
from typing import Optional, Union
from project.models.context_model import ContextModel
from project.models.header_model import HeaderModel
from project.models.menu_item_model import MenuItemModel
from project.models.object_model import ObjectModel
from project.models.property_model import PropertyModel
from project.models.record_type_model import RecordTypeModel
from project.enums import object_enum
from project.records.object_records import object_records
from project.records.menu_records import menu_records
from project.records.context_records import context_records


def get_menu_records() -> list[Union[HeaderModel, MenuItemModel]]:
    """
    Get menu records.
    """
    return menu_records


def get_context_records() -> list[ContextModel]:
    """
    Get context records.
    """
    return context_records
