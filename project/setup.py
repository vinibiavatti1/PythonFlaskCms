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
from project.services import property_service
from project.services import translation_service
import os


###############################################################################
# Register functions
###############################################################################


def register_upload_folder(app: Flask) -> None:
    """
    Register the folder to upload filder.
    """
    app.config['UPLOAD_FOLDER'] = os.path.join(str(app.static_folder), 'files')


def register_secret_key(app: Flask) -> None:
    """
    Set secret key to flask app.
    """
    app.secret_key = SECRET


def register_blueprints(app: Flask) -> None:
    """
    Register all flask blueprints.
    """
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def register_properties() -> None:
    """
    Set properties into database.
    """
    for context_record in context_records:
        context = context_record.code
        for prop in property_records:
            if isinstance(prop, PropertyModel):
                val = property_service.get_property(context, prop.name)
                if val is None:
                    property_service.set_property(
                        context,
                        prop.name,
                        prop.default
                    )


def register_translations() -> None:
    """
    Add translations to database.
    """
    for context_record in context_records:
        context = context_record.code
        for translation in translation_records:
            found = translation_service.select_by_name(
                context,
                translation.name,
            )
            if found is None:
                translation_service.insert(context, translation.__dict__)


def register_users() -> None:
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
    register_secret_key(app)
    register_upload_folder(app)
    register_blueprints(app)
    register_properties()
    register_translations()
    register_users()
    # Add more actions...
