"""
URLs Controller.

This module provide the routes for url management.
"""
from typing import Any
from flask import Blueprint, redirect, render_template, flash, request, url_for
from project.utils.security_utils import login_required
from project.services import sitemap_service
from project.records.special_urls import special_urls


# Blueprint
blueprint = Blueprint(
    'sitemap_ctrl',
    __name__,
    url_prefix='/admin/sitemap'
)


###############################################################################
# View Routes
###############################################################################


@blueprint.route('/')
@login_required()
def index() -> str:
    """
    Index route.
    """
    urls: list[Any] = sitemap_service.select_page_urls()
    urls.extend(special_urls)
    return render_template(
        '/admin/sitemap.html',
        data=dict(
            urls=urls,
        )
    )


###############################################################################
# Action Routes
###############################################################################

'''
@blueprint.route('/insert', methods=['POST'])
@login_required()
def insert() -> Any:
    """
    Insert menu route.
    """
    try:
        menu_id = menu_service.insert(request.form.to_dict())
        flash('Menu created successfully!', category='success')
        return redirect(f'/admin/menus/detail/{menu_id}')
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(f'/admin/menus/create')


@blueprint.route('/update/<menu_id>', methods=['POST'])
@login_required()
def update(menu_id: int) -> Any:
    """
    Update menu route.
    """
    try:
        menu_service.update(menu_id, request.form.to_dict())
        flash('Menu updated successfully!', category='success')
    except Exception as err:
        flash(str(err), category='danger')
    return redirect(f'/admin/menus/detail/{menu_id}')


@blueprint.route('/delete/<menu_id>', methods=['GET'])
@login_required()
def delete(menu_id: int) -> Any:
    """
    Delete menu route.
    """
    try:
        menu_service.delete(menu_id)
        flash('Menu deleted successfully!', category='success')
        return redirect(f'/admin/menus')
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(f'/admin/menus/detail/{menu_id}')


@blueprint.route('/duplicate/<menu_id>/<name>', methods=['GET'])
@login_required()
def duplicate(menu_id: int, name: str) -> Any:
    """
    Duplicate menu route.
    """
    try:
        new_menu_id = menu_service.duplicate(menu_id, name)
        flash('Page duplicated successfully!', category='success')
        return redirect(f'/admin/menus/detail/{new_menu_id}')
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(f'/admin/menus/detail/{menu_id}')
'''
