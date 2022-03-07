from flask import Flask
from project.config import config
from project.registry.blueprints import register_blueprints


# Init Flask application
app = Flask(__name__)
app.secret_key = config['secret_key']
register_blueprints(app)
