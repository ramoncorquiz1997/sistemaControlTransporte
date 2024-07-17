# main_routes.py

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models import DailyUnitRecord, Unit
from forms import DailyUnitRecordForm
from app import db

main_routes_bp = Blueprint('main_routes_bp', __name__)

@main_routes_bp.route('/')
def home():
    return render_template('index.html')

@main_routes_bp.route('/welcome')
@login_required
def welcome():
    return render_template('welcome.html', username=current_user.username)

@main_routes_bp.route('/register_daily_record', methods=['GET', 'POST'])
@login_required
def register_daily_record():
    form = DailyUnitRecordForm()
    if form.validate_on_submit():
        unit = Unit.query.filter_by(id=form.unit_id.data).first()
        if unit:
            daily_record = DailyUnitRecord(
                unit_id=unit.id,
                nombre_chofer=form.nombre_chofer.data,
                fecha=form.fecha.data,
                boleto_inicial=form.boleto_inicial.data,
                boleto_entregado=form.boleto_entregado.data,
                cantidad_dinero_esperado=form.cantidad_dinero_esperado.data,
                dinero_entregado=form.dinero_entregado.data,
                restante=form.restante.data,
                dueño_unidad=form.dueño_unidad.data
            )
            db.session.add(daily_record)
            db.session.commit()
            flash('Registro diario de unidad guardado exitosamente', 'success')
            return redirect(url_for('main_routes_bp.home'))
        else:
            flash('Unidad no encontrada', 'danger')
    return render_template('register_daily_record.html', form=form)
