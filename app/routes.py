from flask import Blueprint

main = Blueprint('main', __name__)

#: import views later after initializing main
# because all views are using the 'main' variable
import app.views
