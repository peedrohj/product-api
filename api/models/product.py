from api import db


class Product(db.Model):
    # set table name to products
    __tablename__ = "products"

    # Set product atributs
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Integer, primary_key=True)
