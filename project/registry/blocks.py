"""
Block configuration module.
"""
from typing import Any
from project.enums import field_types_enum as field


###############################################################################
# Registry
###############################################################################


blocks: dict[str, Any] = {
    'text': {
        'template': 'text.html',
        'properties': {
            'text': field.TEXT,
        },
        'active': True,
    },
    # Add more...
}
