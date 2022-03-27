"""
Media controller.
"""
from typing import Any
from unicodedata import category
from flask import Blueprint, redirect, render_template, request, flash
from project.enums import resource_type_enum
from project.decorators.security_decorators import login_required
from project.properties.article_properties import article_properties
from project.decorators.context_decorators import process_context
from project.services import file_service


# Controller data
CONTROLLER_NAME = 'admin_files_ctrl'
URL_PREFIX = '/<context>/admin/files'
PAGE_TITLE = 'Files'


# Blueprint data
blueprint = Blueprint(
    CONTROLLER_NAME,
    __name__,
    url_prefix=URL_PREFIX
)


###############################################################################
# Routes
###############################################################################


@blueprint.route('/', methods=['GET'], defaults={'page': 1})
@blueprint.route('/<int:page>', methods=['GET'])
@login_required()
@process_context()
def list_view(context: str, page: int = 1) -> Any:
    """
    Render list page.
    """
    files = file_service.select_all(context, page)
    first_page_url = f'/{context}/admin/files'
    prev_page_url = f'/{context}/admin/files/{page - 1 if page != 0 else 1}'
    next_page_url = f'/{context}/admin/files/{page + 1}'
    all_page_url = f'/{context}/admin/files/0'
    return render_template(
        '/admin/files_list.html',
        page_data=dict(
            title=PAGE_TITLE,
            action_url=f'/{context}/admin/files/upload',
            delete_url=f'/{context}/admin/files/delete',
            files=files,
            first_page_url=first_page_url,
            prev_page_url=prev_page_url,
            next_page_url=next_page_url,
            all_page_url=all_page_url,
            page=page,
        )
    )


@blueprint.route('/upload', methods=['POST'])
@login_required()
@process_context()
def upload_action(context: str) -> Any:
    """
    Upload file endpoint.
    """
    try:
        data = request.form.to_dict()
        replace = False
        if data['replace'] == 'true':
            replace = True
        files = request.files.getlist("files")
        file_service.upload_files(files, replace)
        flash('File(s) upload successfully', category='success')
    except Exception as err:
        flash(str(err), category='danger')
    return redirect(request.referrer)


@blueprint.route('/delete/<file_name>', methods=['GET'])
@login_required()
@process_context()
def delete_action(context: str, file_name: str) -> Any:
    """
    Delete file action.
    """
    try:
        file_service.delete_file(file_name)
        flash('File deleted successfully', category='success')
    except Exception as err:
        flash(str(err), category='danger')
    return redirect(request.referrer)
