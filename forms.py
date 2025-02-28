from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, URLField
from wtforms.validators import InputRequired, URL

class AddPetForm(FlaskForm):
    pet_name = StringField('Pet Name', validators=[InputRequired()])
    species = StringField('Species', validators=[InputRequired()])
    photo_url = URLField('Photo URL', validators=[InputRequired(), URL()])
    age = IntegerField('Age', validators=[InputRequired()])
    notes = TextAreaField('Notes')
