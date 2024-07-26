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
from routes.list_daily_records import list_daily_records_bp
from routes.edit_owner import edit_owner_bp
from routes.operator_routes import operator_routes_bp  # Importar el nuevo blueprint

# Verificar si el blueprint ya está registrado antes de registrarlo
if 'register_daily_record_bp' not in app.blueprints:
    app.register_blueprint(register_daily_record_bp, url_prefix='/daily_records')

if 'unit_routes_bp' not in app.blueprints:
    app.register_blueprint(unit_routes_bp, url_prefix='/units')

if 'admin_routes_bp' not in app.blueprints:
    app.register_blueprint(admin_routes_bp, url_prefix='/admin')

if 'list_daily_records_bp' not in app.blueprints:
    app.register_blueprint(list_daily_records_bp, url_prefix='/list')

if 'edit_owner_bp' not in app.blueprints:
    app.register_blueprint(edit_owner_bp, url_prefix='/owners')

if 'operator_routes_bp' not in app.blueprints:
    app.register_blueprint(operator_routes_bp, url_prefix='/operators')  # Registrar el nuevo blueprint

if __name__ == '__main__':
    app.run(debug=True)
