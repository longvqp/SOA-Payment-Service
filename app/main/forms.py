from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, Regexp, NumberRange
from wtforms import HiddenField, StringField, IntegerField, SubmitField, BooleanField


class submitForm(FlaskForm):
     masv_pay = StringField('Student ID:', validators=[DataRequired(), Length(1,8)])
     phonesv_pay = StringField('Phone number: ', validators=[DataRequired()])
     emailsv_pay = StringField('Email: ', validators=[DataRequired()])
     
     masv_dept = StringField('Student ID:', validators=[DataRequired(), Length(1,8)])
     emailsv_dept = StringField('Email: ', validators=[DataRequired()])
     sodu = IntegerField('Fee: ', validators=[NumberRange(min=0)])
     sotien = IntegerField('Fee: ', validators=[NumberRange(min=0)])
     submit = SubmitField(label=('Pay'))

class paymentForm(FlaskForm):
     masv_pay = StringField('Student ID Pay:', validators=[DataRequired(), Length(1,8)])
     phonesv_pay = StringField('Phone number: ', validators=[DataRequired()])
     emailsv_pay = StringField('Email: ', validators=[DataRequired()])
     hidden = HiddenField('IDhidden')
     masv_dept = StringField('Student ID Dept:', validators=[DataRequired(), Length(1,8)])
     namesv_dept = StringField('Name: ', validators=[DataRequired(), Length(200)])
     sotienno = IntegerField('Dept: ', validators=[DataRequired()])
     sodu = IntegerField('Wallet: ', validators=[NumberRange(min=0)])
     sotien = IntegerField('Fee: ', validators=[NumberRange(min=0)])
     agreement = BooleanField('I agree all term.', validators=[DataRequired()])
     submit = SubmitField('Pay')

class purchase_form(FlaskForm):
     mssv = StringField('Student ID:', validators=[DataRequired(), Length(1,8)])
     check = SubmitField()

class UpdateBallanceForm(FlaskForm):
     amount_of_monney = IntegerField('Amount: ', validators=[NumberRange(min=0)])
     submit = SubmitField()

class OTPForm(FlaskForm):
     otp = IntegerField('OTP: ', validators=[DataRequired(), Length(6)])
     submit = SubmitField('Done')
     

class hocphi_form(FlaskForm):
     masv = StringField('Student ID:', validators=[DataRequired(), Length(1,8)])
     semester = StringField('Học Kỳ:', validators=[DataRequired()])