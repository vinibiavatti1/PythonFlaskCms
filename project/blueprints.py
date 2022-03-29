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
    faqs_ctrl,
    files_ctrl,
    landing_pages_ctrl,
    properties_ctrl,
    translation_ctrl,
    articles_ctrl,
    events_ctrl,
    trash_bin_ctrl,
    custom_pages_ctrl,
    post_ctrl,
    news_ctrl,
    redirects_ctrl,
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
    translation_ctrl.blueprint,
    articles_ctrl.blueprint,
    events_ctrl.blueprint,
    trash_bin_ctrl.blueprint,
    custom_pages_ctrl.blueprint,
    post_ctrl.blueprint,
    landing_pages_ctrl.blueprint,
    faqs_ctrl.blueprint,
    news_ctrl.blueprint,
    files_ctrl.blueprint,
    media_ctrl.blueprint,
    redirects_ctrl.blueprint,
]
