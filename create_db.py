from app import app, db, User

with app.app_context():
    db.drop_all()
    db.create_all()

    db.session.add(User(username="admin", email="admin@example.com", password="helloworld1234"))
    db.session.add(User(username="test", email="test@gmail.com", password="helloworld1234"))
    db.session.commit()

