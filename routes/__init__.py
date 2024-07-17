def register_routes(app):
    from .main_routes import main_routes_bp
    from .auth_routes import auth_routes_bp
    from .register_daily_record import register_daily_record_bp
    from .unit_routes import unit_routes_bp
    from .admin_routes import admin_routes_bp

    app.register_blueprint(main_routes_bp)
    app.register_blueprint(auth_routes_bp, url_prefix='/auth')

    # Verificar si el blueprint ya está registrado antes de registrarlo
    if 'register_daily_record_bp' not in app.blueprints:
        app.register_blueprint(register_daily_record_bp, url_prefix='/daily_records')

    if 'unit_routes_bp' not in app.blueprints:
        app.register_blueprint(unit_routes_bp, url_prefix='/units')

    if 'admin_routes_bp' not in app.blueprints:
        app.register_blueprint(admin_routes_bp, url_prefix='/admin')
