from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from models import User, Accionista
from app import db

admin_routes_bp = Blueprint('admin_routes_bp', __name__)

@admin_routes_bp.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash('No tienes permiso para acceder a esta página.', 'danger')
        return redirect(url_for('main_routes_bp.home'))

    users = User.query.all()
    return render_template('admin_dashboard.html', users=users)

@admin_routes_bp.route('/admin/change_role/<int:user_id>')
@login_required
def change_role(user_id):
    if not current_user.is_admin:
        flash('No tienes permiso para acceder a esta página.', 'danger')
        return redirect(url_for('main_routes_bp.home'))
    
    user = User.query.get(user_id)
    if user:
        user.is_admin = not user.is_admin
        db.session.commit()
        flash('Los permisos del usuario han sido actualizados.', 'success')
    return redirect(url_for('admin_routes_bp.admin_dashboard'))

@admin_routes_bp.route('/list_accionistas')
@login_required
def list_accionistas():
    accionistas = Accionista.query.all()
    return render_template('list_accionistas.html', accionistas=accionistas)
