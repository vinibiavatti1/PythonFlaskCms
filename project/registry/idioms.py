"""
Idioms registry.
"""
from typing import Any


###############################################################################
# Registry
###############################################################################


idioms: dict[str, Any] = {
    'en': {
        'name': 'English',
        'default': True,
    },
    'pt': {
        'name': 'Portuguese',
        'default': False,
    },
    'en': {
        'name': 'Spanish',
        'default': False,
    },
    # Add more...
}
