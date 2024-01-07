from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os
from dotenv import load_dotenv

# Initialize the Flask application
app = Flask(__name__)

load_dotenv()

# Replace these values with your MySQL database details
HOST = os.environ.get("HOST")
USER = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
DATABASE = os.environ.get("DATABASE")

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@localhost/python_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Import the routes after initializing db to avoid circular import
from app import routes

# Create the database tables
with app.app_context():
    db.create_all()
