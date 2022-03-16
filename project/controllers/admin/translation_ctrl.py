"""
Translation Controller.

This module provide the routes for tranlations.
"""
from typing import Any
from flask import Blueprint, redirect, render_template, flash, request, url_for
from project.decorators.security_decorators import login_required
from project.services import menu_service, translation_service, history_service
from project.enums import resource_type_enum


# Blueprint
blueprint = Blueprint(
    'translation_ctrl',
    __name__,
    url_prefix='/admin/translations'
)


###############################################################################
# View Routes
###############################################################################


@blueprint.route('/')
@login_required()
def index() -> str:
    """
    Index route to list of translations.
    """
    headers = [
        '#',
        'Idiom',
        'Name',
        'Value',
        'Actions',
    ]
    translations = translation_service.select_all()
    data = []
    for translation in translations:
        translation_id = translation['id']
        data.append(
            (
                translation_id,
                translation['idiom'],
                translation['name'],
                translation['value'],
                f'<a href="/admin/translations/detail/{translation_id}"'
                f'>Details</a>',
            )
        )
    return render_template(
        '/admin/translations.html',
        headers=headers,
        data=data,
    )

@blueprint.route('/create')
@login_required()
def create() -> str:
    """
    Translation create route.
    """
    return render_template(
        '/admin/translation_detail.html',
        edit=False,
        data=dict()
    )


@blueprint.route('/detail/<translation_id>')
@login_required()
def detail(translation_id: int) -> Any:
    """
    Translation detail route.
    """
    data = translation_service.select_by_id(translation_id)
    if data is None:
        flash('Translation not found', category='danger')
        return redirect('/admin/transaltions')
    history = history_service.select_by_resource(
        translation_id,
        resource_type_enum.TRANSLATION,
    )
    return render_template(
        '/admin/translation_detail.html',
        edit=True,
        translation_id=translation_id,
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
    Insert translation route.
    """
    try:
        translation_service.insert(request.form.to_dict())
        flash('Translation created successfully!', category='success')
        return redirect(f'/admin/translations')
    except Exception as err:
        flash(str(err), category='danger')
        return redirect('/admin/translations/create')


@blueprint.route('/update/<translation_id>', methods=['POST'])
@login_required()
def update(translation_id: int) -> Any:
    """
    Update translation route.
    """
    try:
        translation_service.update(translation_id, request.form.to_dict())
        flash('Translation updated successfully!', category='success')
        return redirect(f'/admin/translations')
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(f'/admin/translations/detail/{translation_id}')


@blueprint.route('/delete/<translation_id>', methods=['GET'])
@login_required()
def delete(translation_id: int) -> Any:
    """
    Delete translation route.
    """
    try:
        translation_service.delete(translation_id)
        flash('Translation deleted successfully!', category='success')
        return redirect(f'/admin/translations')
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(f'/admin/translations/detail/{translation_id}')
