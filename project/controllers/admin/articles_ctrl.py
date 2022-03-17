"""
Articles controller.
"""
from typing import Any
from werkzeug.utils import redirect
from flask import Blueprint, request, render_template, flash
from project.validators import auth_validator
from project.services import auth_service


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
def list_view() -> str:
    """
    Render datatable with data.
    """
    headers = [
        '#',
        'Key',
        'Name',
        'Access',
        'Published',
        'Actions',
    ]
    data: list[str] = []
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
def create_view() -> str:
    """
    Render create page.
    """
    return render_template(
        '/admin/article.html',
        page_data=dict()
    )


@blueprint.route('/edit/<article_id>', methods=['GET'])
def edit_view(article_id: int) -> str:
    """
    Render edit page.
    """
    return render_template(
        '/admin/article.html',
        page_data=dict(
            article_id=article_id,
            edit=True,
            article=None
        )
    )


###############################################################################
# Action Routes
###############################################################################


@blueprint.route('/create', methods=['POST'])
def create_action() -> str:
    pass


@blueprint.route('/edit/<article_id>', methods=['POST'])
def edit_action(article_id: int) -> str:
    pass


@blueprint.route('/delete/<article_id>', methods=['POST'])
def delete_action(article_id: int) -> str:
    pass


@blueprint.route('/duplicate/<article_id>', methods=['POST'])
def duplicate_action(article_id: int) -> str:
    pass
