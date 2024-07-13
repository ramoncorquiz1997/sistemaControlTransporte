from flask import Blueprint, render_template, request, redirect, url_for, flash

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        
        # Procesar datos de registro aquí, por ahora solo imprimimos
        print(f"Nombre: {firstname}, Apellido: {lastname}, Correo: {email}")
        
        flash('Registro exitoso', 'success')
        return redirect(url_for('auth_routes.register'))
    
    return render_template('register.html')

@auth_routes.route('/login')
def login():
    return render_template('login.html')
