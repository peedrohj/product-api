
from flask import Flask, jsonify, request
from api import models

# App configurations
app = Flask(__name__)
app.config["DEBUG"] = True  # DEBUG MODE
