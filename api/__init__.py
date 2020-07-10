from flask import Flask, jsonify, request, Blueprint
from api.database import DATABASE_CONNECTION_URI
from flask_sqlalchemy import SQLAlchemy

from api import models
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# App configurations
app.config["DEBUG"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI

# Configure Swagger
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        "app_name": "Product API"
    }
)

app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

# Configure database
db = SQLAlchemy(app)

try:
    print("Trying to create tables...") 
    db.create_all()
    print("Tables created")
except Exception as error:
    print("Error creating table: ", error)