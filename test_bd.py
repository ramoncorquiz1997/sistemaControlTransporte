from app import app, db
from models import Accionista
from datetime import datetime

def populate_accionistas():
    accionistas = [
        Accionista(nombres="Juan", apellido_paterno="Pérez", apellido_materno="Gómez", fecha_nacimiento=datetime(1980, 5, 12), numero_telefonico="5551234567"),
        Accionista(nombres="María", apellido_paterno="López", apellido_materno="Hernández", fecha_nacimiento=datetime(1985, 7, 19), numero_telefonico="5559876543"),
        Accionista(nombres="Carlos", apellido_paterno="García", apellido_materno="Martínez", fecha_nacimiento=datetime(1975, 3, 8), numero_telefonico="5554567890"),
        Accionista(nombres="Ana", apellido_paterno="Rodríguez", apellido_materno="Fernández", fecha_nacimiento=datetime(1990, 2, 25), numero_telefonico="5557654321"),
        Accionista(nombres="Luis", apellido_paterno="Sánchez", apellido_materno="Torres", fecha_nacimiento=datetime(1982, 11, 30), numero_telefonico="5552345678"),
        Accionista(nombres="Laura", apellido_paterno="Ramírez", apellido_materno="Vega", fecha_nacimiento=datetime(1988, 4, 15), numero_telefonico="5558765432"),
        Accionista(nombres="Jorge", apellido_paterno="Flores", apellido_materno="Domínguez", fecha_nacimiento=datetime(1981, 9, 20), numero_telefonico="5553456789"),
        Accionista(nombres="Lucía", apellido_paterno="González", apellido_materno="Pineda", fecha_nacimiento=datetime(1979, 6, 18), numero_telefonico="5556543210"),
        Accionista(nombres="Pedro", apellido_paterno="Morales", apellido_materno="Cruz", fecha_nacimiento=datetime(1987, 8, 22), numero_telefonico="5555678901"),
        Accionista(nombres="Elena", apellido_paterno="Ortiz", apellido_materno="Núñez", fecha_nacimiento=datetime(1984, 10, 14), numero_telefonico="5554321098"),
        Accionista(nombres="Miguel", apellido_paterno="Díaz", apellido_materno="Ramírez", fecha_nacimiento=datetime(1991, 1, 5), numero_telefonico="5556789012"),
        Accionista(nombres="Gabriela", apellido_paterno="Mendoza", apellido_materno="Silva", fecha_nacimiento=datetime(1983, 12, 11), numero_telefonico="5557890123"),
        Accionista(nombres="Fernando", apellido_paterno="Ríos", apellido_materno="Vargas", fecha_nacimiento=datetime(1986, 7, 29), numero_telefonico="5558901234"),
        Accionista(nombres="Patricia", apellido_paterno="Castro", apellido_materno="Aguilar", fecha_nacimiento=datetime(1989, 5, 17), numero_telefonico="5559012345"),
        Accionista(nombres="Sergio", apellido_paterno="Alvarez", apellido_materno="Guzmán", fecha_nacimiento=datetime(1980, 3, 21), numero_telefonico="5550123456"),
    ]

    with app.app_context():
        db.session.bulk_save_objects(accionistas)
        db.session.commit()
        print("Tabla de accionistas llenada exitosamente.")

if __name__ == "__main__":
    populate_accionistas()
