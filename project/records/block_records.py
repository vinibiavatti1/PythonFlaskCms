"""
Block records module.
"""
from typing import Any
from project.enums import property_types_enum as prop_type
from project.models.block_model import BlockModel
from project.models.property_model import PropertyModel


block_records: list[BlockModel] = [
    BlockModel(
        name='header',
        description='Section with header (h1)',
        template='header_block.html',
        properties=[
            PropertyModel(
                name='header',
                label='Header',
                description='',
                property_type=prop_type.STR,
            ),
            PropertyModel(
                name='dark_theme',
                label='Dark Theme',
                description='',
                property_type=prop_type.BOOL,
            )
        ]
    ),
    # Add more.
]