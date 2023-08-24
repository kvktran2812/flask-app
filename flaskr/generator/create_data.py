import random

from flaskr import app, db
from flaskr.models import User
import os


def create_names(file_path: str, number: int = 10):
    f_name = []
    with open(file_path) as f:
        lines = f.readlines()
        for i in range(number):
            l_number = random.randint(0, len(lines))
            name = lines[l_number]
            name = name.replace('\n', '')
            f_name.append(name)
    return f_name


def create_email(first, last):
    email = str.lower(first) + "." + str.lower(last) + "@example.com"
    return email


def create_username(first, last):
    username = str.lower(first) + "_" + str.lower(last)
    return username


if __name__ == "__main__":
    with app.app_context():
        dir_path = os.getcwd()
        first_name_file = os.path.join(dir_path, "first_name.txt")
        last_name_file = os.path.join(dir_path, "last_name.txt")

        db.drop_all()
        db.create_all()

        # create admin
        admin = User(username="admin", email="admin@example.com", password="helloworld1234")
        db.session.add(admin)

        # create 100 users
        n_users = 100
        f_names = create_names(first_name_file, n_users)
        l_names = create_names(last_name_file, n_users)

        for first, last in zip(f_names, l_names):
            email = create_email(first, last)
            username = create_username(first, last)
            user = User(username=username, email=email, password="helloworld1234")
            db.session.add(user)

        db.session.commit()

