"""
Idioms records module.
"""
from project.models.idiom_model import IdiomModel


###############################################################################
# Registry
###############################################################################


idioms: list[IdiomModel] = [
    IdiomModel('en', 'English', True),
    IdiomModel('pt', 'Portuguese', False),
    IdiomModel('es', 'Spanish', False),
    # Add more...
]
