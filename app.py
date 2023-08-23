from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, request, session, request
from flask_session import Session


# create the extension

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)

    def __repr__(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }


@app.route("/users")
def users():
    users_ = User.query.all()
    data = [u.__repr__() for u in users_]
    return data


@app.route("/user/<int:user_id>")
def user_detail(user_id):
    if not session.get("name"):
        return redirect("/login")
    user = User.query.filter_by(id=user_id).first()
    return user.__repr__()


@app.route("/")
def index():
    if not session.get("name"):
        return redirect("/login")
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session["name"] = request.form.get("name")
        return redirect("/")
    if request.method == 'GET' and session.get("name"):
        return redirect("/")
    return render_template("login.html")


@app.route("/logout")
def logout():
    session["name"] = None
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
