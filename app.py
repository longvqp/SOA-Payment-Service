import os

from flask import Flask, render_template

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)

@app.route('/', methods=['GET','SET'])
def index():
    return render_template('index.html')