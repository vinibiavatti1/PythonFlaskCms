"""
Blueprints registry module.
"""
from flask import Blueprint
from project.injections import blueprint as injections
from project.handlers import blueprint as handlers
from project.controllers.public import (
    homepage_ctrl,
    search_ctrl,
)
from project.controllers.admin import (
    auth_ctrl,
    cookie_policy_ctrl,
    faqs_ctrl,
    files_ctrl,
    landing_pages_ctrl,
    menu_ctrl,
    properties_ctrl,
    seo_ctrl,
    sitemap_ctrl,
    translation_ctrl,
    redirect_ctrl,
    block_ctrl,
    articles_ctrl,
    events_ctrl,
    trash_bin_ctrl,
    custom_pages_ctrl,
    post_ctrl,
    news_ctrl,
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
    menu_ctrl.blueprint,
    sitemap_ctrl.blueprint,
    translation_ctrl.blueprint,
    redirect_ctrl.blueprint,
    block_ctrl.blueprint,
    articles_ctrl.blueprint,
    events_ctrl.blueprint,
    trash_bin_ctrl.blueprint,
    custom_pages_ctrl.blueprint,
    post_ctrl.blueprint,
    landing_pages_ctrl.blueprint,
    faqs_ctrl.blueprint,
    news_ctrl.blueprint,
    files_ctrl.blueprint,
]
