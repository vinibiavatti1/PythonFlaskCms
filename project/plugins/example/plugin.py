"""
Example plugin implementation.
"""
from flask import Flask
from project.models.plugin_model import PluginModel


class ExamplePlugin(PluginModel):
    """
    Example plugin implementation.
    """

    def __init__(self) -> None:
        """
        Construct an example plugin.
        """
        super().__init__('my_plugin', (1, 0, 0))

    def setup(self, app: Flask) -> None:
        """
        Setup plugin.
        """


plugin = ExamplePlugin()
