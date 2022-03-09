"""
Page Controller.

This module provide the routes for page.
"""
from typing import Any
from flask import Blueprint, redirect, render_template, flash, request, url_for
from project.utils.security_utils import login_required
from project.services import page_service


# Blueprint
blueprint = Blueprint(
    'pages_ctrl',
    __name__,
    url_prefix='/admin/pages'
)


###############################################################################
# View Routes
###############################################################################


@blueprint.route('/')
@login_required()
def index() -> str:
    """
    Index route to list of pages.
    """
    headers = [
        '#',
        'Name',
        'Active',
        'Created By',
        'Updated By',
        'Created On',
        'Updated On',
        'Actions',
    ]
    pages = page_service.select_all()
    data = []
    for page in pages:
        page_id = page['id']
        data.append(
            (
                page_id,
                page['name'],
                'True' if page['active'] == 1 else 'False',
                page['created_by_name'],
                page['updated_by_name'],
                page['created_on'],
                page['updated_on'],
                f'<a href="/admin/pages/detail/{page_id}">Details</a>',
            )
        )
    return render_template(
        '/admin/pages.html',
        headers=headers,
        data=data,
    )

@blueprint.route('/create')
@login_required()
def create() -> str:
    """
    Page create route.
    """
    return render_template(
        '/admin/page_detail.html',
        edit=False,
        data=dict()
    )


@blueprint.route('/detail/<page_id>')
@login_required()
def detail(page_id: int) -> Any:
    """
    Page detail route.
    """
    data = page_service.select_by_id(page_id)
    if data is None:
        flash('Page not found', category='danger')
        return redirect(url_for('.index'))
    page_url = page_service.generate_page_url(
        request.url_root,
        data['idiom'],
        data['name'],
    )
    return render_template(
        '/admin/page_detail.html',
        edit=True,
        page_id=page_id,
        data={
            **data,
            'page_url': page_url
        }
    )


###############################################################################
# Action Routes
###############################################################################


@blueprint.route('/insert', methods=['POST'])
@login_required()
def insert() -> str:
    """
    Insert page route.
    """
    try:
        page_id = page_service.insert(request.form.to_dict())
        flash('Page created successfully!', category='success')
        return render_template(
            '/admin/page_detail.html',
            edit=True,
            page_id=page_id,
            data=dict()
        )
    except Exception as err:
        flash(str(err), category='danger')
        return render_template(
            '/admin/page_detail.html',
            edit=False,
            page_id=None,
            data={}
        )


@blueprint.route('/update/<page_id>', methods=['POST'])
@login_required()
def update(page_id: int) -> str:
    """
    Update page route.
    """
    try:
        page_service.update(page_id, request.form.to_dict())
        flash('Page updated successfully!', category='success')
        return render_template(
            '/admin/page_detail.html',
            edit=True,
            page_id=page_id,
            data=dict()
        )
    except Exception as err:
        flash(str(err), category='danger')
        return render_template(
            '/admin/page_detail.html',
            edit=True,
            page_id=page_id,
            data=dict()
        )
