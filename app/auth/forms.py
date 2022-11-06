from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from ..models import User
from wtforms import ValidationError

class LoginForm(FlaskForm):
    masv = StringField('Student ID:', validators=[DataRequired(), Length(1,10)])
    password = PasswordField('Password:', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class RegisterForm(FlaskForm):
    masv = StringField('Student ID: ',validators=[DataRequired(), Length(1,10)])
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    name = StringField('Name', validators=[DataRequired(), Length(1, 64),])
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data.lower()).first():
            raise ValidationError('Email already registered.')
