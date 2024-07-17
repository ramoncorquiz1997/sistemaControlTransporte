from datetime import datetime
from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Accionista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(50), nullable=False)
    apellido_paterno = db.Column(db.String(50), nullable=False)
    apellido_materno = db.Column(db.String(50), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    numero_telefonico = db.Column(db.String(20), nullable=False)

class Operator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(50), nullable=False)
    apellido_paterno = db.Column(db.String(50), nullable=False)
    apellido_materno = db.Column(db.String(50), nullable=False)
    fecha_nacimiento = db.Column(db.Date, nullable=False)
    numero_telefonico = db.Column(db.String(20), nullable=False)

class Unit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    modelo = db.Column(db.String(50), nullable=False)
    ano = db.Column(db.Integer, nullable=False)
    matricula = db.Column(db.String(20), unique=True, nullable=False)
    dueño_id = db.Column(db.Integer, db.ForeignKey('accionista.id'), nullable=False)
    dueño = db.relationship('Accionista', backref=db.backref('units', lazy=True))

class DailyUnitRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    unit_id = db.Column(db.Integer, db.ForeignKey('unit.id'), nullable=False)
    operador_id = db.Column(db.Integer, db.ForeignKey('operator.id'), nullable=False)
    nombre_chofer = db.Column(db.String(100), nullable=False)
    fecha = db.Column(db.Date, default=datetime.utcnow, nullable=False)
    boleto_inicial = db.Column(db.String(50), nullable=False)
    boleto_entregado = db.Column(db.String(50), nullable=False)
    cantidad_dinero_esperado = db.Column(db.Float, nullable=False)
    dinero_entregado = db.Column(db.Float, nullable=False)
    restante = db.Column(db.Float, nullable=False)
    dueño_unidad = db.Column(db.String(100), nullable=False)
    unit = db.relationship('Unit', backref=db.backref('daily_records', lazy=True))
    operador = db.relationship('Operator', backref=db.backref('daily_records', lazy=True))
