from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, request, session, make_response
from flask_session import Session


# create the extension
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config['SECRET_KEY'] = 'MY_TEST_SECRET_KEY'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)
db = SQLAlchemy(app)


def create_app():
    return app


from flaskr.models import *
from flaskr.routes import *

