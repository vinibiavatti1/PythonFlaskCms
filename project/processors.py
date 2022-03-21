"""
Context processors module.
"""
from typing import Any
from project.models.menu_item_model import MenuItemModel
from project.utils.security_utils import is_authenticated, has_permission
from project.utils.cookie_utils import cookie_policy_consent
from flask import Blueprint, g
from project.records.menu_records import menu_records
from project.records.context_records import context_records
from project.services import property_service
from project.utils import datetime_utils
from project.utils import page_utils


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
    context = g.context
    for menu in menu_records:
        if isinstance(menu, MenuItemModel):
            menu.context = context
    return dict(
        records=dict(
            menu_records=menu_records,
            context_records=context_records,
        )
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
