from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from app import db
from models import Accionista
from forms import EditOwnerForm

edit_owner_bp = Blueprint('edit_owner_bp', __name__)

@edit_owner_bp.route('/edit_owner/<int:owner_id>', methods=['GET', 'POST'])
@login_required
def edit_owner(owner_id):
    owner = Accionista.query.get_or_404(owner_id)
    form = EditOwnerForm(obj=owner)

    if form.validate_on_submit():
        owner.nombres = form.nombres.data
        owner.apellido_paterno = form.apellido_paterno.data
        owner.apellido_materno = form.apellido_materno.data
        owner.fecha_nacimiento = form.fecha_nacimiento.data
        owner.numero_telefonico = form.numero_telefonico.data
        
        try:
            db.session.commit()
            flash('Los datos del accionista han sido actualizados.', 'success')
            return redirect(url_for('admin_routes_bp.list_accionistas'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error al actualizar los datos: {e}', 'danger')

    return render_template('edit_owner.html', form=form, owner=owner)
