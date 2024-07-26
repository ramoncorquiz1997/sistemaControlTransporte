import logging
from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, request
from flask_login import login_required, current_user
from app import db
from models import DailyUnitRecord, Unit, Accionista, Operator
from forms import DailyUnitRecordForm

register_daily_record_bp = Blueprint('register_daily_record_bp', __name__)

@register_daily_record_bp.route('/register', methods=['GET', 'POST'])
@login_required
def create_daily_record():
    form = DailyUnitRecordForm()
    if form.validate_on_submit():
        daily_record = DailyUnitRecord(
            unit_id=form.unit_id.data,
            operador_id=form.operador_id.data,
            nombre_chofer=form.operador_nombre.data,
            fecha=form.fecha.data,
            boleto_inicial=form.boleto_inicial.data,
            boleto_entregado=form.boleto_entregado.data,
            cantidad_dinero_esperado=form.cantidad_dinero_esperado.data,
            dinero_entregado=form.dinero_entregado.data,
            restante=form.restante.data,
            dueño_unidad=form.dueño_unidad.data
        )
        try:
            db.session.add(daily_record)
            db.session.commit()
            flash('Registro diario guardado con éxito', 'success')
        except Exception as e:
            db.session.rollback()
            logging.error(f'Error al guardar el registro: {e}')
            flash(f'Error al guardar el registro: {e}', 'danger')
        return redirect(url_for('register_daily_record_bp.create_daily_record'))
    else:
        logging.info('Formulario no válido')
        for field, errors in form.errors.items():
            for error in errors:
                logging.error(f'Error en el campo {field}: {error}')
                flash(f'Error en el campo {field}: {error}', 'danger')
    return render_template('register_daily_record.html', form=form)

@register_daily_record_bp.route('/get_unit_owner', methods=['POST'])
@login_required
def get_unit_owner():
    unit_id = request.json.get('unit_id')
    unit = Unit.query.filter_by(id=unit_id).first()
    if unit:
        owner = Accionista.query.filter_by(id=unit.dueño_id).first()
        if owner:
            return jsonify({'owner_name': f"{owner.nombres} {owner.apellido_paterno} {owner.apellido_materno}"})
    return jsonify({'owner_name': ''})

@register_daily_record_bp.route('/search_operators', methods=['GET'])
@login_required
def search_operators():
    query = request.args.get('q')
    results = []
    if query:
        operators = Operator.query.filter(
            Operator.nombres.ilike(f'%{query}%') | 
            Operator.apellido_paterno.ilike(f'%{query}%') |
            Operator.apellido_materno.ilike(f'%{query}%')
        ).all()
        results = [{'id': op.id, 'name': f"{op.nombres} {op.apellido_paterno} {op.apellido_materno}"} for op in operators]
    return jsonify(results)

@register_daily_record_bp.route('/list', methods=['GET'])
@login_required
def list_daily_records():
    daily_records = DailyUnitRecord.query.all()
    return render_template('list_daily_records.html', daily_records=daily_records)
