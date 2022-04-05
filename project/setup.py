"""
Setup app functions.
"""
from flask import Flask
from project.entities.object_entity import ObjectEntity
from project.models.property_model import PropertyModel
from project.services import user_service
from project.blueprints import blueprints
from project.enums.security_enum import SECRET
from project.records.user_records import user_records
from project.records.property_records import property_records
from project.records.translation_records import translation_records
from project.records.context_records import context_records
from project.services import property_service
from project.services import object_service
from project.enums import object_subtype_enum, object_type_enum
import os


###############################################################################
# Register functions
###############################################################################


def register_upload_folder(app: Flask) -> None:
    """
    Register the folder to upload filder.
    """
    app.logger.info('Registering upload folder...')
    app.config['UPLOAD_FOLDER'] = os.path.join(str(app.static_folder), 'files')


def register_secret_key(app: Flask) -> None:
    """
    Set secret key to flask app.
    """
    app.logger.info('Registering secret key...')
    app.secret_key = SECRET


def register_blueprints(app: Flask) -> None:
    """
    Register all flask blueprints.
    """
    app.logger.info('Registering blueprints...')
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def register_properties(app: Flask) -> None:
    """
    Set properties into database.
    """
    app.logger.info('Registering properties...')
    for context_record in context_records:
        context = context_record.code
        for prop in property_records:
            if isinstance(prop, PropertyModel):
                found = property_service.property_exists(context, prop.name)
                if not found:
                    property_service.set_property(
                        context,
                        prop.name,
                        prop.default
                    )


def register_translations(app: Flask) -> None:
    """
    Add translations to database.
    """
    app.logger.info('Registering translations...')
    for context_record in context_records:
        context = context_record.code
        for translation in translation_records:
            found = object_service.select_by_name(
                context,
                object_type_enum.RESOURCE,
                object_subtype_enum.TRANSLATION_RESOURCE,
                translation.name,
            )
            if found is None:
                entity = ObjectEntity(
                    context=context,
                    name=translation.name,
                    object_type=object_type_enum.RESOURCE,
                    object_subtype=object_subtype_enum.TRANSLATION_RESOURCE,
                    properties=dict(
                        value=translation.value,
                        active=True,
                    )
                )
                object_service.insert(entity)


def register_users(app: Flask) -> None:
    """
    Register default admin users.
    """
    app.logger.info('Registering users...')
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
    register_properties(app)
    register_translations(app)
    register_users(app)
    # Add more actions...
