"""
News controller.
"""
from typing import Any
from flask import Blueprint, request
from project.enums import resource_type_enum
from project.decorators.security_decorators import login_required
from project.properties.news_properties import news_properties
from project.decorators.context_decorators import process_context
from project.processors import content_ctrl_processor


# Controller data
CONTROLLER_NAME = 'admin_news_ctrl'
URL_PREFIX = '/<context>/admin/news'
PAGE_TITLE = 'News'
LIST_NAME = 'news'
RESOURCE_TYPE = resource_type_enum.NEWS_CONTENT
PROPERTIES = news_properties


# Blueprint data
blueprint = Blueprint(
    CONTROLLER_NAME,
    __name__,
    url_prefix=URL_PREFIX
)


###############################################################################
# Routes
###############################################################################


@blueprint.route('/', methods=['GET'])
@login_required()
@process_context()
def list_view(context: str) -> Any:
    """
    Render datatable with data.
    """
    return content_ctrl_processor.process_list_view(
        context,
        RESOURCE_TYPE,
        LIST_NAME,
        PAGE_TITLE,
    )


@blueprint.route('/create', methods=['GET'])
@login_required()
@process_context()
def create_view(context: str) -> Any:
    """
    Render create page.
    """
    return content_ctrl_processor.process_create_view(
        context,
        RESOURCE_TYPE,
        LIST_NAME,
        PAGE_TITLE,
        PROPERTIES,
    )


@blueprint.route('/edit/<content_id>', methods=['GET'])
@login_required()
@process_context()
def edit_view(context: str, content_id: int) -> Any:
    """
    Render edit page.
    """
    return content_ctrl_processor.process_edit_view(
        context,
        RESOURCE_TYPE,
        LIST_NAME,
        PAGE_TITLE,
        PROPERTIES,
        content_id,
    )


@blueprint.route('/create', methods=['POST'])
@login_required()
@process_context()
def create_action(context: str) -> Any:
    """
    Insert content to database.
    """
    return content_ctrl_processor.process_create_action(
        context,
        RESOURCE_TYPE,
        request.form.to_dict(),
        LIST_NAME,
    )


@blueprint.route('/edit/<content_id>', methods=['POST'])
@login_required()
@process_context()
def edit_action(context: str, content_id: int) -> Any:
    """
    Update content in database.
    """
    return content_ctrl_processor.process_edit_action(
        context,
        RESOURCE_TYPE,
        request.form.to_dict(),
        LIST_NAME,
        content_id,
    )


@blueprint.route('/delete/<content_id>', methods=['GET'])
@login_required()
@process_context()
def delete_action(context: str, content_id: int) -> Any:
    """
    Delete content from database.
    """
    return content_ctrl_processor.process_delete_action(
        context,
        LIST_NAME,
        content_id,
    )


@blueprint.route('/duplicate/<content_id>/<to_context>/<new_name>',
                 methods=['GET'])
@login_required()
@process_context()
def duplicate_action(context: str, content_id: int, to_context: str,
                     new_name: str) -> Any:
    """
    Duplicate content.
    """
    return content_ctrl_processor.process_duplicate_action(
        context,
        LIST_NAME,
        content_id,
        to_context,
        new_name,
    )
