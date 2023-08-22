from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from market.model import Item

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

db = SQLAlchemy(app)


@app.route("/")
def home():
    return f"Hello World"


@app.route("/items")
def items():
    items_list = Item.query.all()
    item_ = []
    for i in items_list:
        item_.append(i.data())
    return item_


@app.route("/test")
def test_item():
    return {
        "test": "test",
    }

