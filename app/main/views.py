from flask import render_template,flash
from . import main

from .forms import retrieve_info, purchase_form,UpdateBallanceForm
from flask_login import login_user, logout_user, login_required, current_user
from random import randint

from .. import db
from ..models import HocPhi


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/tuition', methods=['GET','POST'])
def tuition():
    form = retrieve_info()
    if form.validate_on_submit():
        hocphi = HocPhi.query.filter_by(masv=form.mssv.data).first()
        if(hocphi):
            return render_template('tuition.html',form=form,hocphi=hocphi)
        else:
            flash('No student found')
    return render_template('tuition.html',form=form)

@main.route('/payment', methods=['GET','POST'])
def payment():
    return render_template('payment.html')

@main.route('/info', methods=['GET','POST'])
def info():
    update_ballance = UpdateBallanceForm()
    if update_ballance.validate_on_submit():
        print(update_ballance.amount_of_monney.data)
        print(current_user.sodu)
        current_user.sodu = current_user.sodu + update_ballance.amount_of_monney.data
        # user = User(sodu=update_ballance.amount_of_monney.data)
        db.session.commit()
    return render_template('info.html',update_ballance=update_ballance)

@main.route('/purchase', methods=['GET', 'POST'])
#@login_required
def purchase():
    form = purchase_form() #Form thanh toán
    if form.validate_on_submit():
        hocphi = HocPhi.query.filter_by(masv=form.masv.data,term=form.term.data).first()
        if hocphi.otp:
            flash('OTP is sent. Check your email, please!!!')
            return redirect(url_for(authOTP))
        otp = "%06d" % randint(0,999999)
        hocphi.otp = otp
        db.session.commit()
        otp = user.generate_confirmation_otp()
        send_email(user.email, 'Confirm Your Purchase',
                   'email/confirm', otp= otp )
        flash('A OTP has been sent to you by email.')
        return redirect(url_for('authOTP', masv = hocphi.masv, term = hocphi.term))
    return render_template('payment.html', form=form)

@main.route('/authOTP/<id>/<term>', methods=['GET', 'POST'])
@login_required
def OTP():
    form = OTPForm()
    if form.validate_on_submit():
        hocphi = HocPhi.query.filter_by(masv=masv,term=term).first()
        if hocphi.otp != form.otp.data:
            flash('OTP incorrect. Check your otp, please!!!')
            return redirect(url_for('authOTP'))
        user = User.query.filter_by(masv=masv).first()
        sodu = user.sodu
        user.sodu = sodu - hocphi.sotien
        hocphi.status = 'Done'
        lichsu = LichSu(hocphi_id=hocphi.id, masv_nop=current_user.masv)
        db.session.add(lichsu)
        db.session.commit()
        flash('Purchase successfully!!!')
        return redirect(url_for('index.html'))
    return render_template('payment.html', form=form)


@main.route('/authOTP')
@login_required
def resend_OTP():
    otp = current_user.generate_reset_otp()
    send_email(user.email, 'Confirm Your Purchase',
                   'email/confirm', otp=otp, user=current_user)
    flash('A new OTP email has been sent to you by email.')
    return redirect(url_for('authOTP'))

   

