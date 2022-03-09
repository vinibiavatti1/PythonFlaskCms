"""
Setup app functions.
"""
from flask import Flask
from project.models.property_model import PropertyModel
from project.services import property_service
from project.records.properties import properties
from project.blueprints import blueprints
from project.enums.security_enum import SECRET


###############################################################################
# Register functions
###############################################################################


def __register_secret_key(app: Flask) -> None:
    """
    Set secret key to flask app.
    """
    app.secret_key = SECRET


def __register_blueprints(app: Flask) -> None:
    """
    Register all flask blueprints.
    """
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def __register_properties() -> None:
    """
    Set properties into database.
    """
    for prop in properties:
        if isinstance(prop, PropertyModel):
            if not property_service.property_exists(prop.name):
                property_service.set_property(prop.name, prop.default)


###############################################################################
# Setup
###############################################################################


def setup(app: Flask) -> None:
    """
    Setup function.
    """
    __register_secret_key(app)
    __register_blueprints(app)
    __register_properties()
    # Add more actions...
