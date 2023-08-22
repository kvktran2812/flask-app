from market.app import db
from market.app import Item
from market.app import app

# db.create_all()

item1 = Item(name="Hat", price=500, barcode="2347865008", desc="This is description 1")
item2 = Item(name="IPhone", price=500, barcode="2347865056", desc="This is description 2")
item3 = Item(name="Jean pants", price=500, barcode="2347865034", desc="This is description 3")

with app.app_context():
    # db.create_all()

    db.session.add(item1)
    db.session.add(item2)
    db.session.add(item3)

    db.session.commit()

