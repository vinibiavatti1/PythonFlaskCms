"""
Context processors module.
"""
from typing import Any
from project.utils.security_utils import is_authenticated, has_permission
from project.utils.cookie_utils import cookie_policy_consent
from flask import Blueprint
from project.properties.menu_properties import menu_properties
from project.properties.blocks import blocks
from project.properties.page_templates import page_templates
from project.properties.idioms import idioms
from project.services import property_service
from project.services import translation_service
from project.services import page_service
from project.utils import datetime_utils
from project.utils import page_utils
from project.utils import cookie_utils


# Blueprint
blueprint = Blueprint(
    'processors',
    __name__
)


###############################################################################
# Processors
###############################################################################


@blueprint.app_context_processor
def inject_records() -> dict[str, Any]:
    """
    Inject records.
    """
    return dict(
        templates=page_templates,
        idioms=idioms,
        blocks=blocks,
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
    return dict(menu=menu_properties)


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


@blueprint.app_context_processor
def inject_translations() -> dict[str, Any]:
    """
    Inject translations.
    """
    session_idiom = cookie_utils.get_idiom('en')
    translations = translation_service.select_all_by_idiom(session_idiom)
    if not translations:
        return dict(i18n={})
    dct = {t['name']: t['value'] for t in translations}
    return dict(i18n=dct)


@blueprint.app_context_processor
def inject_urls() -> dict[str, Any]:
    """
    Inject all website URLs.
    """
    return dict(urls=page_service.get_all_website_urls())
