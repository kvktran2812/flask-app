from app import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }

