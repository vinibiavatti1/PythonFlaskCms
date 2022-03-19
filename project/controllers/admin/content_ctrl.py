"""
Content controller.
"""
from typing import Any
from werkzeug.utils import redirect
from flask import Blueprint, request, flash
from project.services import content_service
from project.decorators.security_decorators import login_required
from project.properties.idioms import idioms


# Blueprint
blueprint = Blueprint(
    'admin_content_ctrl',
    __name__,
    url_prefix='/admin/content'
)


###############################################################################
# Action Routes
###############################################################################


@blueprint.route('/create', methods=['POST'])
@login_required()
def create_action() -> Any:
    """
    Insert content to database.
    """
    try:
        data = request.form.to_dict()
        back_url = data['back_url']
        del data['back_url']
        content_service.insert(data)
        flash('Content created successfully!', category='success')
        return redirect(back_url)
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)


@blueprint.route('/edit/<content_id>', methods=['POST'])
@login_required()
def edit_action(content_id: int) -> Any:
    """
    Update content in database.
    """
    try:
        data = request.form.to_dict()
        back_url = data['back_url']
        del data['back_url']
        content_service.update(content_id, data)
        flash('Content updated successfully!', category='success')
        return redirect(back_url)
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)


@blueprint.route('/delete/<content_id>/<list_name>', methods=['GET'])
@login_required()
def delete_action(content_id: int, list_name: str) -> Any:
    """
    Delete content from database.
    """
    try:
        content_service.delete(content_id)
        flash('Content sent to trash bin!', category='success')
        return redirect('/admin/' + list_name)
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)


@blueprint.route('/duplicate/<article_id>/<list_name>/<idiom>',
                 methods=['GET'])
@login_required()
def duplicate_action(content_id: int, list_name: str, idiom: str) -> Any:
    """
    Duplicate content.
    """
    try:
        content_service.duplicate(content_id, idiom)
        flash('Content duplicated successfully!', category='success')
        return redirect('/admin/' + list_name)
    except Exception as err:
        flash(str(err), category='danger')
        return redirect(request.referrer)
