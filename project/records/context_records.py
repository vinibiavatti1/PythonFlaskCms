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
    ContextModel(
        code='pt',
        name='Portuguese',
        description='Portuguese context',
    ),
    ContextModel(
        code='es',
        name='Spanish',
        description='Spanish context',
    ),
    # Add more...
]
