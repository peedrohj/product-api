from flask import Flask, jsonify, request
from api.database import DATABASE_CONNECTION_URI
from flask_sqlalchemy import SQLAlchemy
from api import models

# App configurations
app = Flask(__name__)

# DEBUG MODE
app.config["DEBUG"] = True  
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI

db = SQLAlchemy(app)