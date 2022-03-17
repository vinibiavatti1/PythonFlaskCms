"""
Page templates records module.
"""
from project.models.label_value_model import LabelValueModel


page_templates: list[LabelValueModel] = [
    LabelValueModel(
        label='Landing Page Template (Page with Blocks)',
        value='landing_page_template.html',
    ),
    LabelValueModel(
        label='Static Template (HTML, CSS and JS)',
        value='static_template.html',
    ),
    LabelValueModel(
        label='Blog Template',
        value='blog_template.html',
    ),
    LabelValueModel(
        label='FAQ Template',
        value='faq_template.html',
    ),
    LabelValueModel(
        label='Login Template',
        value='login_template.html',
    ),
    # Add more...
]
