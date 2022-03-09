"""
Setup app functions.
"""
from project.models.property_model import PropertyModel
from project.services import property_service
from project.registry.properties import properties


def setup() -> None:
    """
    Setup function.
    """
    # Setup properties
    for prop in properties:
        if isinstance(prop, PropertyModel):
            if not property_service.property_exists(prop.name):
                property_service.set_property(prop.name, prop.default)

