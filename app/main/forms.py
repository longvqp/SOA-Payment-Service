from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import StringField, PasswordField, BooleanField, SubmitField


class retrieve_info(FlaskForm):
     mssv = StringField('Student ID:', validators=[DataRequired(), Length(1,8)])
     submit = SubmitField()
