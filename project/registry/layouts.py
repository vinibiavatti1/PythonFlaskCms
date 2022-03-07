"""
Layout records.

The layouts registry contains the available layouts listed in templates/layouts
directory. The registered layouts will be avaiable for usange as page layout.
"""
from typing import Any


###############################################################################
# Registry
###############################################################################


layouts: list[str] = [
    'website_layout.html',
    # Add more...
]
