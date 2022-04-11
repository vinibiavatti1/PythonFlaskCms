"""
Blueprints registry module.
"""
from flask import Blueprint
from project.injections import blueprint as injections
from project.handlers import blueprint as handlers
from project.controllers.public import (
    homepage_ctrl,
    search_ctrl,
    seo_ctrl,
    cookie_policy_ctrl,
    media_ctrl,
)
from project.controllers.admin import (
    auth_ctrl,
    files_ctrl,
    properties_ctrl,
    trash_bin_ctrl,
    objects_ctrl,
    import_export_ctrl,
)


###############################################################################
# Registry
###############################################################################


blueprints: list[Blueprint] = [
    injections,
    handlers,
    seo_ctrl.blueprint,
    homepage_ctrl.blueprint,
    cookie_policy_ctrl.blueprint,
    search_ctrl.blueprint,
    properties_ctrl.blueprint,
    auth_ctrl.blueprint,
    trash_bin_ctrl.blueprint,
    files_ctrl.blueprint,
    media_ctrl.blueprint,
    objects_ctrl.blueprint,
    import_export_ctrl.blueprint,
]
