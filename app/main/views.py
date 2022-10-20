from flask import render_template
from . import main
from .forms import LoginForm

@main.route('/')
def index():
    form = LoginForm()
    return render_template('index.html',form=form)
