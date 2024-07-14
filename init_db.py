from app import app, db
from models import User
from sqlalchemy import text

with app.app_context():
    print("Configuración de la base de datos:", app.config['SQLALCHEMY_DATABASE_URI'])
    print("Iniciando la creación de las tablas...")
    try:
        db.create_all()
        print("Tablas creadas exitosamente.")
        
        # Verificar si la tabla User existe
        result = db.session.execute(text("SELECT name FROM sqlite_master WHERE type='table' AND name='user';"))
        tables = result.fetchall()
        if tables:
            print("La tabla 'User' ha sido creada.")
        else:
            print("La tabla 'User' no ha sido creada.")
        
    except Exception as e:
        print("Error al crear las tablas:", e)
