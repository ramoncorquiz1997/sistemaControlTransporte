from flask import Blueprint, render_template
from flask_login import login_required
from models import DailyUnitRecord

list_daily_records_bp = Blueprint('list_daily_records_bp', __name__)

@list_daily_records_bp.route('/list_daily_records')
@login_required
def list_daily_records():
    records = DailyUnitRecord.query.all()
    return render_template('list_daily_records.html', records=records)
