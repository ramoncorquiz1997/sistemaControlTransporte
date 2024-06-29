from flask import render_template, redirect, url_for, request, Blueprint

auth_routes = Blueprint('auth_routes', __name__)

@auth_routes.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtener los datos del formulario
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        
        # Aquí puedes añadir la lógica para validar y procesar los datos del formulario
        print(f"Nombre: {firstname}, Apellido: {lastname}, Correo: {email}")

        # Después de procesar los datos, redirige a una página de inicio o dashboard
        return redirect(url_for('main_routes.index'))
    
    # Si es GET, simplemente muestra el formulario de inicio de sesión
    return render_template('login.html')
