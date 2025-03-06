from flask import Flask, render_template, redirect, url_for
from db import db  # Import db from the db.py file
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from forms import AddPetForm, EditPetForm
from models import Pet

# Initialize the Flask app
app = Flask(__name__)

# Configure the app with your database URI and secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize the db object with the app
db.init_app(app)  # Ensure this is used instead of db = SQLAlchemy(app)

migrate = Migrate(app, db)

# Route for the home page
@app.route('/')
def home():
    return redirect(url_for('pets_list'))  # Redirect to the pets list page

# Route for listing pets
@app.route('/pets')
def pets_list():
    pets = Pet.query.all()  # Get all pets from the database
    return render_template('pets_list.html', pets=pets)

# Route for adding a pet
@app.route('/add-pet', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        new_pet = Pet(
            name=form.name.data,
            species=form.species.data,
            photo_url=form.photo_url.data,
            age=form.age.data,
            available=form.available.data,
            notes=form.notes.data
        )
        db.session.add(new_pet)
        db.session.commit()
        return redirect(url_for('home'))  # or 'pets_list' if you want to go back to the list

    return render_template('add_pet.html', form=form)

# Route for editing a pet
@app.route('/pets/edit/<int:id>', methods=['GET', 'POST'])
def edit_pet(id):
    pet = Pet.query.get_or_404(id)  # Fetch the pet from the database by ID

    form = EditPetForm(obj=pet)  # Pre-fill the form with the pet data

    if form.validate_on_submit():
        # Update the pet fields with the new form data
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        # Commit the changes to the database
        db.session.commit()

        return redirect(url_for('pets_list'))  # Redirect to the pets list page after saving changes

    return render_template('edit_pet.html', form=form, pet=pet)  # Render the form to edit the pet

# Debug route for checking the pets in the database (useful for debugging)
@app.route('/debug-pets')
def debug_pets():
    pets = Pet.query.all()
    print(pets)  # Print the pets to the console for debugging
    return "Check your terminal/log"

# Main entry point to run the app
if __name__ == "__main__":
    app.run(debug=True)
