from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required
from models import Unit

unit_routes_bp = Blueprint('unit_routes_bp', __name__)

@unit_routes_bp.route('/list')
@login_required
def list_units():
    units = Unit.query.all()
    return render_template('list_units.html', units=units)
