from .main_routes import main_routes
from .auth_routes import auth_routes
from .admin_routes import admin_routes

def register_routes(app):
    app.register_blueprint(main_routes)
    app.register_blueprint(auth_routes)
    app.register_blueprint(admin_routes)
