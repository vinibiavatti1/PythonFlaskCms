"""
Context records module.
"""
from project.models.context_model import ContextModel


context_records: list[ContextModel] = [
    ContextModel(
        code='en',
        name='English',
        description='English context',
    ),
    # Add more...
]
