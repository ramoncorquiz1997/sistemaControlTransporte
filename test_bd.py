from app import app, db
from models import User

with app.app_context():
    # Encuentra el usuario por nombre de usuario
    user = User.query.filter_by(username='ramoncorquiz').first()
    
    if user:
        user.is_admin = True
        db.session.commit()
        print(f"El usuario {user.username} ahora es administrador.")
    else:
        print("Usuario no encontrado.")
