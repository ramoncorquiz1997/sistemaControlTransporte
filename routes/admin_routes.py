from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from models import User
from app import db

admin_routes = Blueprint('admin_routes', __name__)

@admin_routes.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash('No tienes permiso para acceder a esta página.', 'danger')
        return redirect(url_for('main_routes.home'))

    users = User.query.all()
    return render_template('admin_dashboard.html', users=users)

@admin_routes.route('/admin/change_role/<int:user_id>')
@login_required
def change_role(user_id):
    if not current_user.is_admin:
        flash('No tienes permiso para acceder a esta página.', 'danger')
        return redirect(url_for('main_routes.home'))
    
    user = User.query.get(user_id)
    if user:
        user.is_admin = not user.is_admin
        db.session.commit()
        flash('Los permisos del usuario han sido actualizados.', 'success')
    return redirect(url_for('admin_routes.admin_dashboard'))
