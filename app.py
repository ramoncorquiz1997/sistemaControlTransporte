from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin
from dotenv import load_dotenv
from config import Config

load_dotenv()  # Cargar variables de entorno desde el archivo .env

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'auth_routes.login'
login_manager.login_message_category = 'info'

# Importar el modelo de usuario
from models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

from routes import register_routes
register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
