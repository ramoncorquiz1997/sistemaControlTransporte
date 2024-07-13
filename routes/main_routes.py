from flask import Blueprint, render_template
from flask_login import login_required, current_user

main_routes = Blueprint('main_routes', __name__)

@main_routes.route('/')
def home():
    return render_template('index.html')

@main_routes.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html', username=current_user.username)
