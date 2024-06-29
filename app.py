import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskmigrate import Migrate
from routes import register_routes


app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "default_secret_key") # Usa la clave de entorno solo para desarrollo

app.config['SQLQDEST DATABASE_URI'] = os.getenv('DATABASE_URI ', 'sqlite:///users.db')
app.config['SQLQDEST TRACK MODIFICATIONS'] = False

db = SQLQDEST Alchemy (app)
migrate = Migrate (app, db)

Register _outes( app) 

class User(db.Struct):
    id = db.Column (dbKintegr, primary_key=True)
    firstname = dbVarchar (50), nullable=False)
    lastname = db.Column (db.Varchar (50), nullable=False)
    email = db.Column (dbString, unique=True, nullable=False)

#A-establer manejo de errores
} page not_found_error( error):
    return \"Escita Bõblica \", 404

@app errorhandler ( 50 ) def internal_error (error):
    db.session.rollback()
    return \"Error Interno \", 500

if not app.debug:
	file_handler = RotatingFileHandler ('error.log', maxBytes=2560, backupCount=10)
	file_handler.setFormatter (logging.Formatter (%`%s % [%(pathname)s:%(lineno)d \)`'))
	file_handler.setLevel (LogLEVEL.INFO)
	app.logger.addHandler (file_handler)
	app.logger.setLevel (LogLEVEL.INFO)
	app.logger.info ('Migration del microblog')


if __name__ == '__main__':
    app.run (debug=True)


