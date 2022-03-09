"""
Context processors module.
"""
from typing import Any
from project.utils.security_utils import is_authenticated, has_permission
from project.utils.cookie_utils import cookie_policy_consent
from flask import Blueprint
from project.registry.menu import menu
from project.registry.page_templates import page_templates
from project.registry.page_layouts import layouts
from project.registry.idioms import idioms
from project.services import property_service
from project.utils import datetime_utils
from project.utils import page_utils


# Blueprint
blueprint = Blueprint('processors', __name__)


###############################################################################
# Processors
###############################################################################


@blueprint.app_context_processor
def inject_registries() -> dict[str, Any]:
    """
    Inject registries.
    """
    return dict(
        templates=page_templates,
        layouts=layouts,
        idioms=idioms
    )


@blueprint.app_context_processor
def inject_python_resources() -> dict[str, Any]:
    """
    Inject common resources to be used in Jinja templates.
    """
    return dict(
        isinstance=isinstance,
        zip=zip,
        enumerate=enumerate,
        len=len,
        str=str
    )


@blueprint.app_context_processor
def inject_security_resources() -> dict[str, Any]:
    """
    Inject security resources to Jinja templates.
    """
    return dict(
        is_authenticated=is_authenticated,
        has_permission=has_permission,
        cookie_policy_consent=cookie_policy_consent(),
    )


@blueprint.app_context_processor
def inject_menu() -> dict[str, Any]:
    """
    Inject the sidenav menus by user authentication.
    """
    return dict(menu=menu)


@blueprint.app_context_processor
def inject_utilities() -> dict[str, Any]:
    """
    Inject utilities.
    """
    return dict(
        generate_title=page_utils.generate_title,
        format_date_to_str=datetime_utils.format_date_to_str,
        format_datetime_to_str=datetime_utils.format_datetime_to_str,
    )


@blueprint.app_context_processor
def inject_properties() -> dict[str, Any]:
    """
    Inject the global properties.
    """
    return dict(properties=property_service.select_all())
