from flask import Blueprint, render_template
from models import Unit

unit_routes = Blueprint('unit_routes', __name__)

@unit_routes.route('/list')
def list_units():
    units = Unit.query.all()
    return render_template('list_units.html', units=units)
