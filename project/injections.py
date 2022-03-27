"""
Injection resources module.
"""
from typing import Any
from project.models.menu_item_model import MenuItemModel
from project.utils.security_utils import is_authenticated, has_permission
from project.utils.cookie_utils import cookie_policy_consent
from flask import Blueprint, g
from project.records.menu_records import menu_records
from project.records.context_records import context_records
from project.services import property_service, file_service
from project.utils import datetime_utils
from project.utils import page_utils
from project.utils import context_utils
from project.services import content_service
from project.enums import file_type_enum


# Blueprint
blueprint = Blueprint(
    'injections',
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
    context = context_utils.get_current_context()
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
    context = context_utils.get_current_context()
    if not context:
        return dict()
    return dict(
        properties=property_service.select_all(context)
    )


@blueprint.app_context_processor
def inject_urls() -> dict[str, Any]:
    """
    Inject the URLs.
    """
    context = context_utils.get_current_context()
    if not context:
        return dict()
    content_urls = content_service.select_all_urls(context, True)
    return dict(
        urls=dict(
            content_urls=content_urls,
            page_urls=[]
        )
    )


@blueprint.app_context_processor
def inject_files() -> dict[str, Any]:
    """
    Inject the files.
    """
    images = file_service.select_all_by_type(file_type_enum.IMAGE)
    videos = file_service.select_all_by_type(file_type_enum.VIDEO)
    files = file_service.select_all_by_type(file_type_enum.FILE)
    return dict(
        files=dict(
            images=images,
            videos=videos,
            files=files,
        )
    )
