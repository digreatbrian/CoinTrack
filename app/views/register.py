from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user
from app.models import User, db
from app.forms import RegistrationForm
from app.routes import main


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        login_user(user)
        flash('Registration successful. You are now logged in.')
        return redirect(url_for('main.dashboard'))
    else:
        if request.method == 'POST':
            flash('Please make sure that all fields are provided with correct input!', 'error')
    return render_template('register.html', form=form)
