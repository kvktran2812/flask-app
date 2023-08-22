from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

db = SQLAlchemy(app)


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=30), nullable=False, unique=True)
    barcode = db.Column(db.String(length=10), nullable=False, unique=True)
    price = db.Column(db.Integer(), nullable=False)
    desc = db.Column(db.String(length=1000), nullable=False, unique=True)

    def __repr__(self):
        return f"Item {self.id}: {self.name}, ${self.price}, {self.barcode}"

    def data(self):
        return {
            "id": self.id,
            "name": self.name,
            "barcode": self.barcode,
            "price": self.price,
            "desc": self.desc,
        }


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