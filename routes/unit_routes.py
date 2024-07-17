# unit_routes.py

from flask import Blueprint, render_template
from flask_login import login_required
from models import Unit

unit_routes_bp = Blueprint('unit_routes_bp', __name__)

@unit_routes_bp.route('/list_units')
@login_required
def list_units():
    units = Unit.query.all()
    return render_template('list_units.html', units=units)
