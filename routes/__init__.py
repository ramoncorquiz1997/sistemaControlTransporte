from .main_routes import main_routes
from .auth_routes import auth_routes
from .admin_routes import admin_routes_bp as admin_routes_bp_unique
from .unit_routes import unit_routes_bp as unit_routes_bp_unique
from .register_daily_record import register_daily_record_bp as register_daily_record_bp_unique

def register_routes(app):
    app.register_blueprint(main_routes)
    app.register_blueprint(auth_routes)
    app.register_blueprint(admin_routes_bp_unique, url_prefix='/admin')
    app.register_blueprint(unit_routes_bp_unique, url_prefix='/units')
    app.register_blueprint(register_daily_record_bp_unique, url_prefix='/daily_records')
