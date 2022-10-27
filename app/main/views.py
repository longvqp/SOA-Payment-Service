from flask import render_template
from . import main
from .forms import retrieve_info,UpdateBallanceForm
from flask_login import current_user
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
        current_user.sodu = current_user.sodu + update_ballance.amount_of_monney.data
        # user = User(sodu=update_ballance.amount_of_monney.data)
        db.session.commit()
    return render_template('info.html',update_ballance=update_ballance)