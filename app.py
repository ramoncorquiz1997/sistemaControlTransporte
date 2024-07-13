from flask import Flask, render_template
from routes.auth_routes import auth_routes

app = Flask(__name__)

app.register_blueprint(auth_routes, url_prefix='/auth')

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
