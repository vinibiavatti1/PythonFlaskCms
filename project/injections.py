"""
Injection resources module.
"""
from typing import Any
from project.models.menu_item_model import MenuItemModel
from project.utils.security_utils import is_authenticated, has_permission
from project.utils.cookie_utils import cookie_policy_consent
from flask import Blueprint
from project.records.menu_records import menu_records
from project.records.context_records import context_records
from project.services import property_service
from project.services import file_service
from project.services import object_service
from project.utils import datetime_utils
from project.utils import page_utils
from project.utils import context_utils
from project.utils import str_utils
from project.enums import object_type_enum
from project.enums import object_subtype_enum
from project.enums import file_type_enum
from project.models.url_model import UrlModel


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
    if not context:
        return dict()
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
        utils=dict(
            generate_title=page_utils.generate_title,
            format_date_to_str=datetime_utils.format_date_to_str,
            format_datetime_to_str=datetime_utils.format_datetime_to_str,
            title=str_utils.title
        )
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
    contents = object_service.select_by_type(
        context,
        object_type_enum.CONTENT
    )
    pages = object_service.select_by_type(
        context,
        object_type_enum.PAGE
    )
    resources = object_service.select_by_type(
        context,
        object_type_enum.RESOURCE
    )
    content_urls = [
        UrlModel.map_from_object_entity(content) for content in contents
    ]
    page_urls = [
        UrlModel.map_from_object_entity(page) for page in pages
    ]
    resource_urls = [
        UrlModel.map_from_object_entity(resource) for resource in resources
    ]
    return dict(
        urls=dict(
            content_urls=content_urls,
            page_urls=page_urls,
            resource_urls=resource_urls,
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


@blueprint.app_context_processor
def inject_translations() -> dict[str, Any]:
    """
    Inject translations.
    """
    context = context_utils.get_current_context()
    if not context:
        return dict()
    translations = object_service.select_by_type_and_subtype(
        context,
        object_type_enum.RESOURCE,
        object_subtype_enum.TRANSLATION_RESOURCE,
    )
    return dict(
        i18n={t.name: t.properties['value'] for t in translations}
    )
