"""
Page layouts records module.
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