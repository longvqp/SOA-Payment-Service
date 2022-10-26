from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, Regexp, NumberRange
from wtforms import StringField, IntegerField, SubmitField


class retrieve_info(FlaskForm):
     mssv = StringField('Student ID:', validators=[DataRequired(), Length(1,8)])
     submit = SubmitField()

class UpdateBallanceForm(FlaskForm):
     amount_of_monney = IntegerField('Amount: ', validators=[NumberRange(min=0)])
     submit = SubmitField()