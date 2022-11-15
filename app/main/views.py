from flask import render_template,flash,jsonify, redirect,url_for, request
from . import main
from .forms import purchase_form,UpdateBallanceForm, paymentForm, OTPForm
from flask_login import login_user, logout_user, login_required, current_user
from random import randint
from .. import db
from ..models import HocPhi, User
from ..email import send_email


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/tuition/<mssv>')
@login_required
def fee(mssv):
    hocphi = HocPhi.query.filter_by(masv=str(mssv), status='Wait').first()
    hocphi1 = HocPhi.query.filter_by(masv=str(mssv), status='Pending').first()
    user = User.query.filter_by(masv=str(mssv)).first()
    if hocphi1 is not None:
        return jsonify({ 'error' : 'Tài khoản đang trong quá trình thanh toán.'})
    if hocphi is None:
        sotien = "None"
        idd = "None"
    else: 
        sotien =hocphi.sotien
        idd = hocphi.id

    return jsonify({ 'name' : user.name, 'hocphi' : sotien , 'id' : idd})


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
        print(current_user.sodu)
        print(hocphi.sotien)
        print(hocphi.id)
        if(current_user.sodu >= hocphi.sotien):
            if hocphi.otp:
                flash('OTP is sent. Check your email, please!!!')
                return redirect(url_for('main.authOTP', idd=hocphi.id))
            otp = hocphi.generate_confirmation_otp()
            # print(otp)
            send_email(current_user.email, 'Confirm Your Purchase',
                   'authOTP', otp= otp , user=current_user)
            flash('A OTP has been sent to you by email.')
            return redirect(url_for('main.authOTP', idd=hocphi.id, masv=hocphi.masv)) 
        else:
            flash('You dont have enought ballance')
            return redirect(url_for('main.purchase', form=form1)) 
    return render_template('purchase.html', form=form1)

@main.route('/authOTP', methods=['GET', 'POST'])
@login_required
def authOTP():
    form = OTPForm()
    idd  = (request.args['idd'])
    hocphi = HocPhi.query.get(idd)
    if form.is_submitted():
        print("OTP:" ,form.otp.data)
        print("Hoc phi", hocphi.id)    
        
        user = User.query.filter_by(masv=hocphi.masv).first() #User được nộp tiền
        if form.otp.data is None:
            flash('vui lòng nhập OTP') #validation
        
        if hocphi.confirm(form.otp.data, current_user.id, hocphi.id):
            db.session.commit()
            flash('Purchase successfully!!!')
            send_email(current_user.email, 'Purchase successfully.', #gửi email thành công cho người nộp
                   'index',  user=current_user)
            send_email(user.email, 'Purchase successfully.', #gửi email thành công cho người được nộp
                   'index' , user=user)
            return redirect(url_for('main.index'))
        flash("Đã có lỗi xảy ra. Vui lòng kiểm tra mã OTP.")
    url_form=url_for('main.authOTP', idd=idd)
    
    print(url_form)
    return render_template('authOTP.html', form=form, url=url_form)



@main.route('/authOTP/reset')
@login_required
def resend_OTP():
    idd  = int(request.args['id'])
    hocphi = HocPhi.query.get(idd)
    token, otp = hocphi.reset_otp()
    send_email(current_user.email, 'Confirm Your Purchase',
                   'authOTP', otp=otp, user=current_user)
    flash('A new OTP email has been sent to you by email.')
    return redirect(url_for('authOTP', idd=hocphi.id))

