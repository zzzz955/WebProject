from .db import db

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200))

    def __repr__(self):
        return f'<Item {self.name}>'
