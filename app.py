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


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email
        }


@app.route("/users")
def users():
    users_ = User.query.all()
    data = [u.to_json() for u in users_]
    response = make_response(data)
    response.status_code = 200
    return data


@app.route("/user/<int:user_id>")
def user_detail(user_id):
    if not session.get("name"):
        response = make_response("ERROR: user is not login")
        response.status_code = 401
        return response
    user = User.query.filter_by(id=user_id).first()
    if user.username == session.get("name"):
        response = make_response(user.to_json())
        response.status_code = 200
        return response
    else:
        response = make_response("ERROR: permission denied to data")
        response.status_code = 403
        return response


@app.route("/")
def index():
    if not session.get("name"):
        return render_template('login.html')
    return render_template('index.html')


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        name = request.form.get("name")
        password = request.form.get("password")

        user = User.query.filter_by(username=name).first()
        if user:
            if password == user.password:
                session["name"] = name
                response = make_response(user.to_json())
                response.status_code = 200
                return response
    if request.method == 'GET' and session.get("name"):
        response = make_response("User already login")
        response.status_code = 200
        return response
    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    response = make_response("Logout: Clear session")
    response.status_code = 200
    return response


@app.route("/register", methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()

        response = make_response(f"SUCESS: Register successful")
        response.status_code = 200
        return response
    else:
        response = make_response("HTTP Request is not supported")
        response.status_code = 404
        return response


if __name__ == '__main__':
    app.run(debug=True)
