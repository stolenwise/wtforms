from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, URLField, BooleanField
from wtforms.validators import Optional, InputRequired, URL

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Optional, AnyOf, URL, NumberRange

class AddPetForm(FlaskForm):
    pet_name = StringField("Pet Name", validators=[InputRequired()])
    species = StringField(
        "Species",
        validators=[InputRequired(), AnyOf(["cat", "dog", "porcupine"], message="Species must be cat, dog, or porcupine")]
    )
    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL(message="Must be a valid URL")]
    )
    age = IntegerField(
        "Age",
        validators=[Optional(), NumberRange(min=0, max=30, message="Age must be between 0 and 30")]
    )
    notes = TextAreaField("Notes", validators=[Optional()])



class EditPetForm(FlaskForm):
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available?")
