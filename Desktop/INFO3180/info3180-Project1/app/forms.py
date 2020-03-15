from flask_wtf import FlaskForm
from wtforms import Form,StringField, TextAreaField, SelectField, FileField,FileAllowed
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    first_name= StringField('First Name',
                       validators=[DataRequired("Please enter your first name.")])

    last_name=StringField('Last Name',
                       validators=[DataRequired("Please enter your last name.")])

    gender=SelectField('Gender', choices=[('M,Male'), ('F,Female')],
    				validators=[DataRequired("Please enter whether male or female.")])

    
    email= StringField('Email Address',
                        validators=[DataRequired("Please enter your email address."),Email()])

    location = StringField('Location',
    						validators=[DataRequired("Please enter your location.")])
    
    biography= StringField('Biography',
                          validators=[DataRequired("Please enter your biography.")], widget=TextAreaField())
    
    image = FileField('Profile Picture',
                          validators=[DataRequired("Please enter a Profile Picture."),FileAllowed(['jpg','png'], 'Images Only')])

    