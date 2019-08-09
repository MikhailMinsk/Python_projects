from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Configure

app = Flask(__name__)
app.config.from_object(Configure)

db = SQLAlchemy(app)
