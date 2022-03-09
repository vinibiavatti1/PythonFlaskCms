"""
Page templates list.
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
        label='Default Template (Custom HTML, CSS and JS)',
        value='default_template.html',
    ),
    # Add more...
]
