from app import app, db
from models import User, Admin, Unit, Operator, DailyUnitRecord
from sqlalchemy import text

with app.app_context():
    print("Configuración de la base de datos:", app.config['SQLALCHEMY_DATABASE_URI'])
    print("Iniciando la creación de las tablas...")
    try:
        db.create_all()
        print("Tablas creadas exitosamente.")
        
        # Verificar si las tablas existen
        result_admin = db.session.execute(text("SELECT name FROM sqlite_master WHERE type='table' AND name='admin';"))
        tables_admin = result_admin.fetchall()
        if tables_admin:
            print("La tabla 'Admin' ha sido creada.")
        else:
            print("La tabla 'Admin' no ha sido creada.")
        
        result_unit = db.session.execute(text("SELECT name FROM sqlite_master WHERE type='table' AND name='unit';"))
        tables_unit = result_unit.fetchall()
        if tables_unit:
            print("La tabla 'Unit' ha sido creada.")
        else:
            print("La tabla 'Unit' no ha sido creada.")
        
        result_operator = db.session.execute(text("SELECT name FROM sqlite_master WHERE type='table' AND name='operator';"))
        tables_operator = result_operator.fetchall()
        if tables_operator:
            print("La tabla 'Operator' ha sido creada.")
        else:
            print("La tabla 'Operator' no ha sido creada.")
        
        result_daily_unit_record = db.session.execute(text("SELECT name FROM sqlite_master WHERE type='table' AND name='daily_unit_record';"))
        tables_daily_unit_record = result_daily_unit_record.fetchall()
        if tables_daily_unit_record:
            print("La tabla 'DailyUnitRecord' ha sido creada.")
        else:
            print("La tabla 'DailyUnitRecord' no ha sido creada.")
        
    except Exception as e:
        print("Error al crear las tablas:", e)
