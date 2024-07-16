from app import app, db
from models import User

with app.app_context():
    user = User.query.filter_by(username='ramoncorquiz').first()
    if user:
        user.is_admin = True
        db.session.commit()
        print(f"Usuario {user.username} ahora es administrador.")
    else:
        print("Usuario no encontrado.")
