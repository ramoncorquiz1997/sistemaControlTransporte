from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
from config import Config

load_dotenv()  # Cargar variables de entorno desde el archivo .env

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
csrf = CSRFProtect(app)  # Añadir protección CSRF

login_manager = LoginManager(app)
login_manager.login_view = 'auth_routes_bp.login'
login_manager.login_message_category = 'info'

# Importar el modelo de usuario
from models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from routes import register_routes
register_routes(app)

# Importar y registrar los blueprints
from routes.register_daily_record import register_daily_record_bp
from routes.unit_routes import unit_routes_bp
from routes.admin_routes import admin_routes_bp

# Verificar si el blueprint ya está registrado antes de registrarlo
if 'register_daily_record_bp' not in app.blueprints:
    app.register_blueprint(register_daily_record_bp, url_prefix='/daily_records')

if 'unit_routes_bp' not in app.blueprints:
    app.register_blueprint(unit_routes_bp, url_prefix='/units')

if 'admin_routes_bp' not in app.blueprints:
    app.register_blueprint(admin_routes_bp, url_prefix='/admin')

if __name__ == '__main__':
    app.run(debug=True)
