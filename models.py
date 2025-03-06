from db import db  # Import db from app.py directly here

# Define the Pet model using db
class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)
    photo_url = db.Column(db.String(200))
    age = db.Column(db.Integer)
    notes = db.Column(db.String(500))
    available = db.Column(db.Boolean, default=True)




    def image_url(self):
        """Return image for pet -- bespoke or generic."""

        return self.photo_url or GENERIC_IMAGE

    def __repr__(self):
        return f'<Pet {self.pet_name}>'
