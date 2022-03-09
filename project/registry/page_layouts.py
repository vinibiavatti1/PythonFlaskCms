"""
Layout records.

The layouts registry contains the available layouts listed in templates/layouts
directory. The registered layouts will be avaiable for usange as page layout.
"""
from project.models.label_value_model import LabelValueModel


###############################################################################
# Registry
###############################################################################


layouts: list[LabelValueModel] = [
    LabelValueModel(
        label='Default Layout',
        value='default_layout.html'
    ),
    LabelValueModel(
        label='Empty Layout (Without navbar, footers, etc.)',
        value='empty_layout.html'
    ),
    # Add more...
]
