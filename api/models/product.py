from api import db

class Product(db.Model):
    # Set product atributs
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    description = db.Column(db.Text())

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def get_object(self):
        return {
            'id': self.id, 
            'name': self.name,
            'description': self.description,
        }