from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, Regexp, NumberRange
from wtforms import StringField, IntegerField, SubmitField


class submitForm(FlaskForm):
     masv_pay = StringField('Student ID:', validators=[DataRequired(), Length(1,8)])
     emaisv_pay = StringField('Email: ', validators=[DataRequired()])
     masv_dept = StringField('Student ID:', validators=[DataRequired(), Length(1,8)])
     emaisv_dept = StringField('Email: ', validators=[DataRequired()])
     sodu = IntegerField('Fee: ', validators=[NumberRange(min=0)])
     sotien = IntegerField('Fee: ', validators=[NumberRange(min=0)])
     submit = SubmitField(label=('Pay'))

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