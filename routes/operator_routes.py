from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app import db
from models import Operator
from forms import OperatorForm

operator_routes_bp = Blueprint('operator_routes_bp', __name__)

@operator_routes_bp.route('/list_operators')
@login_required
def list_operators():
    operators = Operator.query.all()
    return render_template('list_operators.html', operators=operators)

@operator_routes_bp.route('/edit_operator/<int:operator_id>', methods=['GET', 'POST'])
@login_required
def edit_operator(operator_id):
    operator = Operator.query.get_or_404(operator_id)
    form = OperatorForm(obj=operator)
    if form.validate_on_submit():
        form.populate_obj(operator)
        db.session.commit()
        flash('Datos del operador actualizados correctamente', 'success')
        return redirect(url_for('operator_routes_bp.list_operators'))
    return render_template('edit_operator.html', form=form, operator=operator)

@operator_routes_bp.route('/create_operator', methods=['GET', 'POST'])
@login_required
def create_operator():
    form = OperatorForm()
    if form.validate_on_submit():
        new_operator = Operator(
            nombres=form.nombres.data,
            apellido_paterno=form.apellido_paterno.data,
            apellido_materno=form.apellido_materno.data,
            fecha_nacimiento=form.fecha_nacimiento.data,
            numero_telefonico=form.numero_telefonico.data
        )
        db.session.add(new_operator)
        db.session.commit()
        flash('Nuevo operador creado correctamente', 'success')
        return redirect(url_for('operator_routes_bp.list_operators'))
    return render_template('create_operator.html', form=form)
