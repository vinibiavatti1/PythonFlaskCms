"""
Public page renderization controller.

This module provide the routes for page renderization.
"""
from typing import Any
from flask import Blueprint, redirect, render_template, flash, request, url_for
from project.decorators.security_decorators import login_required
from project.services import page_service, history_service, block_service


# Blueprint
blueprint = Blueprint(
    'public_page_render_ctrl',
    __name__,
    url_prefix='/page'
)


###############################################################################
# View Routes
###############################################################################


@blueprint.route('/<idiom>/<page_name>')
def render_page(idiom: str, page_name: str) -> str:
    """
    Page render controller.
    """
    return render_template(
        '/admin/pages.html',
    )
