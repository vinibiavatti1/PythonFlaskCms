"""
Plugin utilities.
"""
from flask import Flask
import importlib
import os
import sys


ROOT_PATH = sys.path[0]
PLUGINS_FOLDER = os.path.join(ROOT_PATH, 'project', 'plugins')
PLUGINS_PACKAGE = 'project.plugins'
PLUGIN_MODULE_NAME = 'plugin'



def get_plugins() -> list[str]:
    """
    Get plugins on project/plugins folder.
    """
    plugins: list[str] = list()
    plugin_folders = os.listdir(PLUGINS_FOLDER)
    for plugin_folder in plugin_folders:
        plugin_file = os.path.join(PLUGINS_FOLDER, plugin_folder, 'plugin.py')
        if os.path.exists(plugin_file):
            plugins.append(plugin_folder)
    return plugins


def load_plugin(app: Flask, plugin_folder_name: str) -> None:
    """
    Import plugin module to python context.
    """
    module_name = \
        f'{PLUGINS_PACKAGE}.{plugin_folder_name}.{PLUGIN_MODULE_NAME}'
    plugin_module = importlib.import_module(module_name)
    if (plugin_module and
            plugin_module.plugin and
            plugin_module.plugin.load_plugin):
        plugin_module.plugin.load_plugin(app)
