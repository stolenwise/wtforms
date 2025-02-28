from app import db

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pet_name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    photo_url = db.Column(db.String(100))
    age = db.Column(db.Integer)
    notes = db.Column(db.String(200))
    available = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Pet {self.pet_name}>'
