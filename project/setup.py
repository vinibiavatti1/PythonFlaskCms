"""
Setup app functions.
"""
from flask import Flask
from project.models.property_model import PropertyModel
from project.services import user_service
from project.blueprints import blueprints
from project.enums.security_enum import SECRET
from project.records.user_records import user_records
from project.records.property_records import property_records
from project.records.translation_records import translation_records
from project.records.context_records import context_records
from project.repositories import property_repository
from project.repositories import translation_repository


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
    for context_record in context_records:
        context = context_record.name
        for prop in property_records:
            if isinstance(prop, PropertyModel):
                val = property_repository.get_property(context, prop.name)
                if val is None:
                    property_repository.set_property(
                        context,
                        prop.name,
                        prop.default
                    )


def __register_translations() -> None:
    """
    Add translations to database.
    """
    for context_record in context_records:
        context = context_record.name
        for translation in translation_records:
            translation_repository.s
            found = translation_service.select_by_idiom_and_name(
                translation.idiom,
                translation.name,
            )
            if found is None:
                translation_service.insert(translation.__dict__)


def __register_users() -> None:
    """
    Register default admin users.
    """
    for user in user_records:
        found = user_service.select_by_email(user.email)
        if found is None:
            user_service.insert(user.__dict__)


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
    # __register_translations()
    __register_users()
    # Add more actions...
