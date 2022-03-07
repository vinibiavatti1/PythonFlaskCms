from flask import Blueprint, render_template
from json import dumps
from project.utils.security_utils import login_required


# Blueprint
blueprint = Blueprint(
    'idioms',
    __name__,
    url_prefix='/admin/idioms'
)


###############################################################################
# Routes
###############################################################################


@blueprint.route('/')
@login_required()
def index() -> str:
    """
    Index route to list of idioms.
    """
    headers = [
        '#',
        'Name',
        'Code',
        'Created By',
        'Updated By',
        'Created On',
        'Updated On',
        'Actions',
    ]
    data = [
        (
            1,
            'English',
            'en',
            'Vini',
            '-',
            '2021-01-01 02:37:21 am',
            '-',
            f'<a href="/admin/idioms/detail/{1}">Details</a>'
        ),
    ]
    return render_template(
        '/admin/idioms.html',
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
        '/admin/idioms_detail.html',
        data={
            'id': _id,
        }
    )
