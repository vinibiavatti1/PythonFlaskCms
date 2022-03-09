"""
Blueprints registry module.
"""
from flask import Blueprint, Flask
from project.processors import blueprint as processors
from project.handlers import blueprint as handlers
from project.controllers.public import (
    homepage_ctrl,
    locale_ctrl,
    search_ctrl,
)
from project.controllers.admin import (
    auth_ctrl,
    cookie_policy_ctrl,
    map_ctrl,
    chart_ctrl,
    list_ctrl,
    form_ctrl,
    calendar_ctrl,
    pages_ctrl,
    properties_ctrl,
    seo_ctrl,
)


###############################################################################
# Registry
###############################################################################


blueprints: list[Blueprint] = [
    processors,
    handlers,
    seo_ctrl.blueprint,
    homepage_ctrl.blueprint,
    locale_ctrl.blueprint,
    map_ctrl.blueprint,
    chart_ctrl.blueprint,
    list_ctrl.blueprint,
    form_ctrl.blueprint,
    cookie_policy_ctrl.blueprint,
    calendar_ctrl.blueprint,
    search_ctrl.blueprint,
    pages_ctrl.blueprint,
    properties_ctrl.blueprint,
    auth_ctrl.blueprint,
]
