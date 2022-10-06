import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/', methods=['GET','SET'])
def index():
    return render_template('index.html')