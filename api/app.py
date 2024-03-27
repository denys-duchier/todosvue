from flask import Flask
from flask_cors import CORS

cors = CORS(app, resources={r"/api/v1.0/*": {"origins": ["http://127.0.0.1:5000","http://localhost:5000"]}})
app = Flask(__name__)

import os

def mkpath(p):
    return os.path.normpath(
            os.path.join(
                os.path.dirname(__file__),p)
            )

from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = (
    'sqlite:///' + mkpath('../quiz.db')
)

db = SQLAlchemy(app)
