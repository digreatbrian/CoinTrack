from flask import render_template, url_for, redirect
from flask_login import current_user

from app.routes import main


@main.route('/')
def index():
    return render_template('index.html')
