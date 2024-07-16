# register_daily_record.py

from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, request
from flask_login import login_required, current_user
from app import db
from models import DailyUnitRecord, Unit, Admin
from forms import DailyUnitRecordForm

register_daily_record = Blueprint('register_daily_record', __name__)

@register_daily_record.route('/register', methods=['GET', 'POST'])
@login_required
def register_daily_record():
    form = DailyUnitRecordForm()
    if form.validate_on_submit():
        daily_record = DailyUnitRecord(
            unit_id=form.unit_id.data,
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
        flash('Registro diario guardado con éxito', 'success')
        return redirect(url_for('register_daily_record.register_daily_record'))
    return render_template('register_daily_record.html', form=form)

@register_daily_record.route('/get_unit_owner', methods=['POST'])
@login_required
def get_unit_owner():
    unit_id = request.json.get('unit_id')
    unit = Unit.query.filter_by(id=unit_id).first()
    if unit:
        owner = Admin.query.filter_by(id=unit.dueño_id).first()
        if owner:
            return jsonify({'owner_name': f"{owner.nombres} {owner.apellido_paterno} {owner.apellido_materno}"})
    return jsonify({'owner_name': ''})
