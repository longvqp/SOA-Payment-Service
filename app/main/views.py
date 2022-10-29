from flask import render_template
from . import main

from .forms import retrieve_info, purchase_form,UpdateBallanceForm
from flask_login import login_user, logout_user, login_required, current_user
from random import randint

from .. import db


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/tuition')
def tuition():
    form = retrieve_info()
    return render_template('tuition.html',form=form)

@main.route('/info', methods=['GET','POST'])
def info():
    update_ballance = UpdateBallanceForm()
    if update_ballance.validate_on_submit():
        print(update_ballance.amount_of_monney.data)
        print(current_user.sodu)
        current_user.sodu = update_ballance.amount_of_monney.data
        # user = User(sodu=update_ballance.amount_of_monney.data)
        db.session.commit()
    return render_template('info.html',update_ballance=update_ballance)


@main.route('/purchase', methods=['GET', 'POST'])
#@login_required
def purchase():
    form = purchase_form() #Form thanh toán
    form1 = hocphi_form() #form để lấy masv của người được nộp
    if form.validate_on_submit():
        hocphi = HocPhi.query.filter_by(masv=form1.masv.data,semester=form1.semester.data).first()
        if hocphi.otp:
            flash('OTP is sent. Check your email, please!!!')
            return redirect(url_for('authOTP', id=hocphi.id))
        token, otp = hocphi.generate_confirmation_otp()
        send_email(current_user.email, 'Confirm Your Purchase',
                   'email/confirm', otp= otp )
        flash('A OTP has been sent to you by email.')
        return redirect(url_for('authOTP',id = hocphi.id))
    return render_template('payment.html', form=form)

@main.route('/authOTP/<token>')
@login_required
def authOTP(token):
    form = OTPForm()
    if form.validate_on_submit():
        hocphi = HocPhi.query.get(id)
        # if hocphi.otp != form.otp.data:
        #     flash('OTP incorrect. Check your otp, please!!!')
        #     return redirect(url_for('authOTP'))
        user = User.query.filter_by(masv=hocphi.masv).first() #User được nộp tiền
        if hocphi.confirm(token, current_user.id):
            db.session.commit()
            flash('Purchase successfully!!!')
            send_email(current_user.email, 'Purchase successfully.', #gửi email thành công cho người nộp
                   'index' )
            send_email(user.email, 'Purchase successfully.', #gửi email thành công cho người được nộp
                   'index' )
            return redirect(url_for('index.html'))
        flash("Đã có lỗi xảy ra. Vui lòng kiểm tra mã OTP.")
    return redirect(url_for('authOTP', form=form))
     #chưa biết là sau khi redirect thì user và id còn được lưu hay không. trong code được hiểu là nó có lưu lại thông tin



@main.route('/authOTP')
@login_required
def resend_OTP():
    hocphi = HocPhi.query.get(id)
    token, otp = hocphi.generate_reset_otp()
    send_email(current_user.email, 'Confirm Your Purchase',
                   'email/confirm', otp=otp, token= token)
    flash('A new OTP email has been sent to you by email.')
    return redirect(url_for('authOTP', id=hocphi.id))



