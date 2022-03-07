from flask import Blueprint, render_template, flash, request
from json import dumps
from project.utils.security_utils import login_required
from project.errors import ValidationError
from project.validators import page_validator
from project.repositories import page_repository


# Blueprint
blueprint = Blueprint(
    'pages',
    __name__,
    url_prefix='/admin/pages'
)


###############################################################################
# Routes
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
    data = [
        (
            1,
            'homepage',
            'True',
            'Vini',
            '-',
            '2021-01-01 02:37:21 am',
            '-',
            f'<a href="/admin/pages/detail/{1}">Details</a>'
        ),
    ]
    return render_template(
        '/admin/pages.html',
        headers=headers,
        data=data
    )


@blueprint.route('/detail/<_id>')
@login_required()
def detail(_id: int) -> str:
    """
    Landing page detail route.
    """
    return render_template(
        '/admin/page_detail.html',
        data={
            'id': _id,
        }
    )


@blueprint.route('/save/<_id>')
@login_required()
def save(_id: int) -> str:
    """
    Save page data.
    """
    try:
        data = request.form
        page_validator.validate_save_data(data)
        page_repository.save(_id, data)
        flash('Page saved successfully', category='success')
    except Exception as err:
        flash(str(err), category='danger')
    return render_template(
        '/admin/page_detail.html',
        data={
            'id': _id,
        }
    )
