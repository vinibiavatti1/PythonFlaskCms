"""
Plugin model for plugin creations.
"""
from abc import ABC, abstractmethod
from typing import Any
from flask import Flask


class PluginModel(ABC):
    """
    Plugin model class.
    """

    def __init__(self, name: str, version: tuple[int, ...]) -> None:
        """
        Construct a new plugin.

        Parameters
            name: Name of the plugin
            version: Tuple version of the plugin, ex: (1, 0, 3)
        """
        self.name = name
        self.version = version

    @abstractmethod
    def setup(self, app: Flask) -> None:
        """
        Setup plugin on application startup.
        """

    def load_plugin(self, app: Flask) -> None:
        """
        Load plugin and call setup.
        """
        app.logger.info(f'Registering {self.name} plugin...')
        self.setup(app)
