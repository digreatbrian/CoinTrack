from flask import redirect, url_for, flash
from flask_login import login_required, logout_user
from app.routes import main


@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('main.index'))
