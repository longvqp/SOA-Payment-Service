from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, Regexp, NumberRange
from wtforms import StringField, IntegerField, SubmitField


class retrieve_info(FlaskForm):
     mssv = StringField('Student ID:', validators=[DataRequired(), Length(1,8)])
     check = SubmitField()

class purchase_form(FlaskForm):
     mssv = StringField('Student ID:', validators=[DataRequired(), Length(1,8)])
     check = SubmitField()

class UpdateBallanceForm(FlaskForm):
     amount_of_monney = IntegerField('Amount: ', validators=[NumberRange(min=0)])
     submit = SubmitField()

class OTPForm(FlaskForm):
     otp = IntegerField('OTP: ', validators=[DataRequired(), Length(6)])
     submit = SubmitField()



class hocphi_form(FlaskForm):
     masv = StringField('Student ID:', validators=[DataRequired(), Length(1,8)])
     semester = StringField('Học Kỳ:', validators=[DataRequired()])