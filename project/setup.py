"""
Setup app functions.
"""
from flask import Flask
from project.models.property_model import PropertyModel
from project.services import user_service
from project.blueprints import blueprints
from project.enums.security_enum import SECRET
from project.records.builtin_user_records import builtin_user_records
from project.records.property_records import property_records
from project.records.builtin_object_records import \
    builtin_object_records
from project.records.context_records import context_records
from project.services import property_service
from project.services import object_service
from project.utils import plugin_utils
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
    Register builtin properties.
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


def register_builtin_objects(app: Flask) -> None:
    """
    Register builtin objects.
    """
    app.logger.info('Registering builtin objects...')
    for context_record in context_records:
        context = context_record.code
        for builtin_object in builtin_object_records:
            found = object_service.select_by_name(
                context,
                builtin_object.name,
            )
            if found is None:
                object_service.insert_builtin(context, builtin_object)


def register_users(app: Flask) -> None:
    """
    Register builtin admin users.
    """
    app.logger.info('Registering users...')
    for user in builtin_user_records:
        found = user_service.select_by_email(user.email)
        if found is None:
            user_service.insert(user.__dict__)


def register_plugins(app: Flask) -> None:
    """
    Register and install plugins.
    """
    plugins = plugin_utils.get_plugins()
    for plugin in plugins:
        plugin_utils.load_plugin(app, plugin)


###############################################################################
# Setup
###############################################################################


def setup(app: Flask) -> None:
    """
    Setup function.
    """
    # Setup natives
    register_secret_key(app)
    register_upload_folder(app)
    register_blueprints(app)
    register_properties(app)
    register_users(app)
    register_builtin_objects(app)

    # Setup plugins
    register_plugins(app)
