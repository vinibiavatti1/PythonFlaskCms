"""
Block Controller.

This module provide the routes for menu.
"""
from typing import Any
from flask import Blueprint, redirect, render_template, flash, request, url_for
from project.utils.security_utils import login_required
from project.services import block_service, menu_service, history_service
import json


# Blueprint
blueprint = Blueprint(
    'block_ctrl',
    __name__,
    url_prefix='/admin/blocks'
)


###############################################################################
# View Routes
###############################################################################


@blueprint.route('/detail/<block_name>/<page_id>')
@login_required()
def create(block_name: str, page_id: int) -> Any:
    """
    Block create route.
    """
    block_properties = block_service.get_block_properties_by_name(block_name)
    return render_template(
        '/admin/block_detail.html',
        edit=False,
        page_id=page_id,
        block_name=block_name,
        block_properties=block_properties,
    )


@blueprint.route('/edit/<block_id>')
@login_required()
def edit(block_id: int) -> Any:
    """
    Block edit route.
    """
    block = block_service.get_block_by_id(block_id)
    if not block:
        flash('Block not found', category='danger')
        return redirect(f'/admin/pages')
    block_properties = block_service.get_block_properties_by_name(
        block['name']
    )
    property_values = json.loads(block['json'])
    return render_template(
        '/admin/block_detail.html',
        edit=True,
        page_id=block['id_page'],
        block_name=block['name'],
        block_properties=block_properties,
        property_values=property_values,
    )


###############################################################################
# Action Routes
###############################################################################


@blueprint.route('/insert/<block_name>/<page_id>', methods=['POST'])
@login_required()
def insert(block_name: str, page_id: int) -> Any:
    """
    Insert block route.
    """
    try:
        block_id = block_service.insert(
            page_id,
            block_name,
            request.form.to_dict()
        )
        flash('Block added successfully!', category='success')
        return redirect(f'/admin/pages/detail/{page_id}?tab=blocks')
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(f'/admin/blocks/edit/{block_id}')


'''
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
