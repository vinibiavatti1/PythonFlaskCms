"""
Block service.
"""
from typing import Any, Optional
from project.models.property_model import PropertyModel
from project.records.blocks import blocks
from project.repositories import block_repository
import json


def get_block_properties_by_name(block_name: str
                                 ) -> Optional[list[PropertyModel]]:
    """
    Get block properties by name.
    """
    for block in blocks:
        if block.name == block_name:
            return block.properties
    return None


def get_block_by_id(block_id: int
                    ) -> Optional[dict[str, Any]]:
    """
    Get block properties by id.
    """
    return block_repository.select_by_id(block_id)


def select_page_blocks(page_id: int) -> list[dict[str, Any]]:
    """
    Get a list of the page blocks.
    """
    return block_repository.select_all(page_id)


def insert(page_id: int, block_name: str, data: dict[str, Any]) -> Any:
    """
    Insert block into a page.
    """
    return block_repository.insert(
        page_id,
        block_name,
        json.dumps(data)
    )


def save_order(block_ids: list[int], new_orders: list[int]) -> None:
    """
    Save new order for blocks.
    """
    for block_id, new_order in zip(block_ids, new_orders):
        block_repository.update_order(block_id, new_order)
