from flask import render_template, redirect, url_for, flash
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
        flash('Registration successful. You can now log in.')
        login_user(user)
        return redirect(url_for('main.dashboard'))
    return render_template('register.html', form=form)
