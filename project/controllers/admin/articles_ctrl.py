"""
Articles controller.
"""
from typing import Any
from werkzeug.utils import redirect
from flask import Blueprint, request, render_template, flash, abort
from project.models.property_model import PropertyModel
from project.services import content_service
from project.enums import resource_type_enum
from project.decorators.security_decorators import login_required
from project.properties.article_properties import article_properties
from project.utils.data_utils import set_properties_value

# Blueprint
blueprint = Blueprint(
    'admin_articles_ctrl',
    __name__,
    url_prefix='/admin/articles'
)


###############################################################################
# View Routes
###############################################################################


@blueprint.route('/', methods=['GET'])
@login_required()
def list_view() -> str:
    """
    Render datatable with data.
    """
    headers = [
        '#',
        'Name',
        'Private',
        'Published',
        'Created On',
        'Actions',
    ]
    data: list[Any] = list()
    contents = content_service.select_all('en', resource_type_enum.ARTICLE)
    for content in contents:
        id_ = content['id']
        data.append((
            id_,
            content['name'],
            'True' if content['private'] == 1 else 'False',
            'True' if content['published'] == 1 else 'False',
            content['created_on'],
            f'<a href="/admin/articles/edit/{id_}">Details...</a>'
        ))
    return render_template(
        '/admin/datatable.html',
        page_data=dict(
            headers=headers,
            data=data,
            title='Articles',
            btn_label='New Article',
            btn_link='/admin/articles/create',
        )
    )


@blueprint.route('/create', methods=['GET'])
@login_required()
def create_view() -> str:
    """
    Render create page.
    """
    return render_template(
        '/admin/content.html',
        page_data=dict(
            title='Articles',
            back_url='/admin/articles',
            properties=article_properties,
            content_type=resource_type_enum.ARTICLE,
            list_name='articles',
        )
    )


@blueprint.route('/edit/<content_id>', methods=['GET'])
@login_required()
def edit_view(content_id: int) -> str:
    """
    Render edit page.
    """
    content = content_service.select_by_id(content_id)
    if not content:
        abort(404)
    props = set_properties_value(article_properties, content)
    return render_template(
        '/admin/content.html',
        page_data=dict(
            content_id=content_id,
            edit=True,
            article=None,
            title='Articles',
            back_url='/admin/articles',
            properties=props,
            blocks_url='/admin/blocks/' + str(content_id),
            content_type=resource_type_enum.ARTICLE,
            list_name='articles',
        )
    )
