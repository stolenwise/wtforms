from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, URLField, SelectField, BooleanField, SubmitField
from wtforms.validators import InputRequired, URL, Optional, Length, DataRequired

class AddPetForm(FlaskForm):
    name = StringField('Pet Name', validators=[DataRequired()]) 
    species = StringField('Species', validators=[DataRequired()])
    photo_url = StringField('Photo URL')
    age = IntegerField('Age')
    notes = TextAreaField('Notes')
    available = BooleanField('Available', default=True)
    submit = SubmitField('Save')


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    name = StringField('Pet Name', validators=[DataRequired()]) 

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Available?")
