from flask import Flask, render_template, redirect, url_for
from db import db  # Import db from the db.py file
from flask_wtf.csrf import generate_csrf
from forms import AddPetForm, EditPetForm
from models import Pet

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'  
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize db with the app
db.init_app(app)

@app.route('/')
def home():
    return redirect('/pets')

@app.route('/pets')
def pets_list():
    pets = Pet.query.all()  # Get all pets from the database
    return render_template('pets_list.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        pet_name = form.pet_name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        
        # Create a new pet instance
        new_pet = Pet(pet_name=pet_name, species=species, photo_url=photo_url, age=age, notes=notes)

        existing_pet = Pet.query.filter_by(pet_name=pet_name, species=species).first()
        if existing_pet is None:

            # Add to session and commit
            db.session.add(new_pet)
            db.session.commit()
        
        # Redirect to home or another page
        return redirect(url_for('home'))

    return render_template('add_pet.html', form=form)


@app.route('/pets/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet) #pre fill with the pet data

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

 
        db.session.commit()
        return redirect(url_for('pets_list'))
    
    return render_template('edit_pet.html', pet=pet, form=form)


@app.route('/pets/<int:pet_id>/delete', methods=['POST'])
def delete_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    db.session.delete(pet)
    db.session.commit()
    return redirect(url_for('pets_list'))

@app.context_processor
def csrf_token():
    return dict(csrf_token=generate_csrf)


if __name__ == "__main__":
    app.run(debug=True)
