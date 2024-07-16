from .main_routes import main_routes
from .auth_routes import auth_routes
from .admin_routes import admin_routes
from .register_daily_record import register_daily_record
from .unit_routes import unit_routes

def register_routes(app):
    app.register_blueprint(main_routes)
    app.register_blueprint(auth_routes)
    app.register_blueprint(admin_routes)

def register_routes(app):
    app.register_blueprint(main_routes)
    app.register_blueprint(auth_routes)
    app.register_blueprint(admin_routes, url_prefix='/admin')
    app.register_blueprint(register_daily_record, url_prefix='/daily_records')
    app.register_blueprint(unit_routes, url_prefix='/units')