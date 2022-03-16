"""
Blueprints registry module.
"""
from flask import Blueprint
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
    menu_ctrl,
    page_ctrl,
    properties_ctrl,
    seo_ctrl,
    sitemap_ctrl,
    translation_ctrl,
    redirect_ctrl,
    block_ctrl,
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
    # map_ctrl.blueprint,
    # chart_ctrl.blueprint,
    # list_ctrl.blueprint,
    # form_ctrl.blueprint,
    cookie_policy_ctrl.blueprint,
    # calendar_ctrl.blueprint,
    search_ctrl.blueprint,
    page_ctrl.blueprint,
    properties_ctrl.blueprint,
    auth_ctrl.blueprint,
    menu_ctrl.blueprint,
    sitemap_ctrl.blueprint,
    translation_ctrl.blueprint,
    redirect_ctrl.blueprint,
    block_ctrl.blueprint,
]
