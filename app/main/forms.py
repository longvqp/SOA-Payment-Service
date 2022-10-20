from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import StringField, PasswordField, BooleanField, SubmitField


class LoginForm(FlaskForm):
    mssv = StringField('Msvv', validators=[DataRequired(), Length(1,10)])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')
