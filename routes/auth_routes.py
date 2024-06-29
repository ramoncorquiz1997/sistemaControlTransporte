from flask import render_template, redirect, url_for, request, Blueprint
from app import db, User

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']

        new_user = User(firstname=firstname, lastname=lastname, email=email)
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('auth_routes.login'))
    
    return render_template('register.html')

@auth_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('main_routes.index'))

    return render_template('login.html')
