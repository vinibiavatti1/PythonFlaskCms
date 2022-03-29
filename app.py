"""
Application entry point.
"""
from flask import Flask
from project.setup import setup


###############################################################################
# App Initialization
###############################################################################


# Init Flask application
app = Flask(__name__)
setup(app)
app.logger.info('Application started!')
