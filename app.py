from flask import Flask, render_template
from routes import register_routes

app = Flask(__name__)
app.secret_key = 'ramon'  # Añade una clave secreta para sesiones

# Configura las rutas
register_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
