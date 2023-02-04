from flask import Flask
from routes.routes import routes_bp, authentication_bp
from flask_jwt_extended import JWTManager
from config import Config

# Created the Flask app
app = Flask(__name__)

# Registering route Blueprint
app.register_blueprint(routes_bp)
app.register_blueprint(authentication_bp)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = Config.SECRET_KEY
jwt = JWTManager(app)
app.config["JWT_ALGORITHM"] = Config.JWT_ALGORITHM

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
