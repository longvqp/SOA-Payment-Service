from flask import render_template
from . import main
from .forms import retrieve_info


@main.route('/')
def index():
    return render_template('index.html')

@main.route('/tuition')
def tuition():
    form = retrieve_info()
    return render_template('tuition.html',form=form)

@main.route('/info')
def info():
    return render_template('info.html')