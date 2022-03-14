"""
Redirect Controller.

This module provide the routes for redirects.
"""
from typing import Any
from flask import Blueprint, redirect, render_template, flash, request, url_for
from project.utils.security_utils import login_required
from project.services import redirect_service, history_service
from project.enums import resource_type_enum


# Blueprint
blueprint = Blueprint(
    'redirect_ctrl',
    __name__,
    url_prefix='/admin/redirects'
)


###############################################################################
# View Routes
###############################################################################


@blueprint.route('/')
@login_required()
def index() -> str:
    """
    Index route to list of redirects.
    """
    headers = [
        '#',
        'From URL (Regex)',
        'To URL',
        'Actions',
    ]
    redirects = redirect_service.select_all()
    data = []
    for redirect in redirects:
        redirect_id = redirect['id']
        from_url = redirect['from_url']
        to_url = redirect['to_url']
        data.append(
            (
                redirect_id,
                f'<span class="font-monospace">{from_url}</span>',
                f'<span class="font-monospace">{to_url}</span>',
                f'<a href="/admin/redirects/detail/{redirect_id}"'
                f'>Details</a>',
            )
        )
    return render_template(
        '/admin/redirects.html',
        headers=headers,
        data=data,
    )

@blueprint.route('/create')
@login_required()
def create() -> str:
    """
    Redirect create route.
    """
    return render_template(
        '/admin/redirect_detail.html',
        edit=False,
        data=dict()
    )


@blueprint.route('/detail/<redirect_id>')
@login_required()
def detail(redirect_id: int) -> Any:
    """
    Redirect detail route.
    """
    data = redirect_service.select_by_id(redirect_id)
    if data is None:
        flash('Redirect not found', category='danger')
        return redirect('/admin/transaltions')
    history = history_service.select_by_resource(
        redirect_id,
        resource_type_enum.REDIRECT,
    )
    return render_template(
        '/admin/redirect_detail.html',
        edit=True,
        redirect_id=redirect_id,
        data={
            **data,
            'history': history
        }
    )


###############################################################################
# Action Routes
###############################################################################


@blueprint.route('/insert', methods=['POST'])
@login_required()
def insert() -> Any:
    """
    Insert redirect route.
    """
    try:
        redirect_service.insert(request.form.to_dict())
        flash('Redirect created successfully!', category='success')
        return redirect(f'/admin/redirects')
    except Exception as err:
        flash(str(err), category='danger')
        return redirect('/admin/redirects/create')


@blueprint.route('/update/<redirect_id>', methods=['POST'])
@login_required()
def update(redirect_id: int) -> Any:
    """
    Update redirect route.
    """
    try:
        redirect_service.update(redirect_id, request.form.to_dict())
        flash('Redirect updated successfully!', category='success')
        return redirect(f'/admin/redirects')
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(f'/admin/redirects/detail/{redirect_id}')


@blueprint.route('/delete/<redirect_id>', methods=['GET'])
@login_required()
def delete(redirect_id: int) -> Any:
    """
    Delete redirect route.
    """
    try:
        redirect_service.delete(redirect_id)
        flash('Redirect deleted successfully!', category='success')
        return redirect(f'/admin/redirects')
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(f'/admin/redirects/detail/{redirect_id}')
