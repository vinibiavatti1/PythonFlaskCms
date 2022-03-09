"""
Block records module.
"""
from typing import Any
from project.enums import property_types_enum as prop_type


###############################################################################
# Registry
###############################################################################


blocks: dict[str, Any] = {
    'text': {
        'template': 'text.html',
        'properties': {
            'text': prop_type.TEXT,
        },
        'active': True,
    },
    # Add more...
}
