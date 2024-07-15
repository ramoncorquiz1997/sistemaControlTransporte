from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, current_user, logout_user, login_required
from app import db, bcrypt
from models import User
from forms import RegistrationForm, LoginForm

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main_routes.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        print(f"Usuario registrado: {user}")  # Esto es solo para verificación en consola
        flash('Tu cuenta ha sido creada! Ahora puedes iniciar sesión', 'success')
        return redirect(url_for('auth_routes.login'))
    return render_template('register.html', form=form)

@auth_routes.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main_routes.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main_routes.home'))
        else:
            flash('Error al iniciar sesión. Por favor verifica usuario y contraseña', 'danger')
    return render_template('login.html', form=form)

@auth_routes.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main_routes.home'))
