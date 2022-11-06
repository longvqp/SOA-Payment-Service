from flask import render_template,flash,jsonify, redirect,url_for
from . import main
from .forms import submitForm, purchase_form,UpdateBallanceForm, hocphi_form, paymentForm, OTPForm
from flask_login import login_user, logout_user, login_required, current_user
from random import randint
from .. import db
from ..models import HocPhi, User
from ..email import send_email


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/tuition', methods=['GET','POST'])
def tuition():
    info_form = submitForm()
    info_form.masv_pay = current_user.masv
    info_form.emaisv_pay = current_user.email
    info_form.masv_dept = None
    info_form.emaisv_dept = None
    info_form.sodu = current_user.sodu
    info_form.sotien = None
    if info_form.validate_on_submit():
        print('sdfsdfsdfsdfsdfsdf')
        return redirect(url_for('/payment')) 
    return render_template('tuition.html', info_form=info_form)

@main.route('/payment/<id>', methods=['GET','POST'])
def payment(id):
    print(id)
    student_indept = User.query.filter_by(masv=id).first()
    fee = HocPhi.query.filter_by(masv=id).first()
    return render_template('payment.html',student_indept=student_indept,fee=fee)


@main.route('/tuition/<mssv>')
@login_required
def fee(mssv):
    hocphi = HocPhi.query.filter_by(masv=str(mssv), status='Wait').first()
    user = User.query.filter_by(masv=str(mssv)).first()
    if hocphi is None:
        sotien = "None"
        idd = "None"
    else: 
        sotien =hocphi.sotien
        idd = hocphi.id

    return jsonify({ 'name' : user.username, 'hocphi' : sotien , 'id' : idd})


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
@login_required
def purchase():
    # form = purchase_form() #Form thanh toán
    form1 = paymentForm()
    if form1.is_submitted():
        idd = int(form1.hidden.data)
        hocphi = HocPhi.query.get(idd)
        if hocphi.otp:
            flash('OTP is sent. Check your email, please!!!')
            return redirect(url_for('authOTP', id=hocphi.id))

        otp = hocphi.generate_confirmation_otp()
        print(otp)
        send_email(current_user.email, 'Confirm Your Purchase',
                   'authOTP', otp= otp , user=current_user)
        flash('A OTP has been sent to you by email.')
        return redirect(url_for('main.authOTP', idd=hocphi.id)) 
    
    return render_template('purchase.html', form=form1)

@main.route('/authOTP', methods=['GET', 'POST'])
@login_required
def authOTP():
    form = OTPForm()
    idd  = int(request.args['idd'])
    if form.validate_on_submit():
        hocphi = HocPhi.query.get(idd)
        
        user = User.query.filter_by(masv=hocphi.masv).first() #User được nộp tiền
        if form.otp.data is None:
            flash('vui lòng nhập OTP') #validation
        
        if hocphi.confirm(form.otp.data, current_user.id):
            db.session.commit()
            flash('Purchase successfully!!!')
            send_email(current_user.email, 'Purchase successfully.', #gửi email thành công cho người nộp
                   'index' )
            send_email(user.email, 'Purchase successfully.', #gửi email thành công cho người được nộp
                   'index' )
            return redirect(url_for('index.html'))
        flash("Đã có lỗi xảy ra. Vui lòng kiểm tra mã OTP.")
    return render_template('authOTP.html', form=form)



@main.route('/authOTP/reset')
@login_required
def resend_OTP():
    hocphi = HocPhi.query.get(id)
    token, otp = hocphi.reset_otp()
    send_email(current_user.email, 'Confirm Your Purchase',
                   'authOTP', otp=otp, user=current_user)
    flash('A new OTP email has been sent to you by email.')
    return redirect(url_for('authOTP', id))

