"""
Page templates records module.
"""
from project.models.label_value_model import LabelValueModel


###############################################################################
# Registry
###############################################################################


page_templates: list[LabelValueModel] = [
    LabelValueModel(
        label='Landing Page Template (Page with Blocks)',
        value='landing_page_template.html',
    ),
    LabelValueModel(
        label='Static Template (HTML, CSS and JS)',
        value='static_template.html',
    ),
    # Add more...
]
