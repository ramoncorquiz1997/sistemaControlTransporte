from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField, DateField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from models import User


class RegistrationForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar contraseña', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrarse')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Este usuario no está disponible, escoge otro')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Este usuario ya tiene un registro, favor de usar otro')

class LoginForm(FlaskForm):
    username = StringField('Usuario', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember = BooleanField('Recuérdame')
    submit = SubmitField('Iniciar sesión')

# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class DailyUnitRecordForm(FlaskForm):
    unit_id = StringField('Número de Unidad', validators=[DataRequired()])
    operador_nombre = StringField('Nombre del Operador', validators=[DataRequired()])
    operador_id = HiddenField('ID del Operador', validators=[DataRequired()])
    fecha = DateField('Fecha', format='%Y-%m-%d', validators=[DataRequired()])
    boleto_inicial = StringField('Boleto Inicial', validators=[DataRequired()])
    boleto_entregado = StringField('Boleto Entregado', validators=[DataRequired()])
    cantidad_dinero_esperado = FloatField('Cantidad de Dinero Esperado', validators=[DataRequired()])
    dinero_entregado = FloatField('Dinero Entregado', validators=[DataRequired()])
    restante = FloatField('Restante', validators=[DataRequired()])
    dueño_unidad = StringField('Dueño de la Unidad', validators=[DataRequired()])
    submit = SubmitField('Registrar')


class EditOwnerForm(FlaskForm):
    nombres = StringField('Nombres', validators=[DataRequired()])
    apellido_paterno = StringField('Apellido Paterno', validators=[DataRequired()])
    apellido_materno = StringField('Apellido Materno', validators=[DataRequired()])
    fecha_nacimiento = DateField('Fecha de Nacimiento', format='%Y-%m-%d', validators=[DataRequired()])
    numero_telefonico = StringField('Número Telefónico', validators=[DataRequired()])
    submit = SubmitField('Actualizar')

class OperatorForm(FlaskForm):
    nombres = StringField('Nombres', validators=[DataRequired()])
    apellido_paterno = StringField('Apellido Paterno', validators=[DataRequired()])
    apellido_materno = StringField('Apellido Materno', validators=[DataRequired()])
    fecha_nacimiento = DateField('Fecha de Nacimiento', validators=[DataRequired()], format='%Y-%m-%d')
    numero_telefonico = StringField('Número Telefónico', validators=[DataRequired()])
    submit = SubmitField('Actualizar')


