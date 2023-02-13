from flask import Flask
from routes.routes import routes_bp, authentication_bp
from flask_jwt_extended import JWTManager
from config import Config
from flask_sqlalchemy import SQLAlchemy

# Created the Flask app
app = Flask(__name__)

# Registering route Blueprint
app.register_blueprint(routes_bp)
app.register_blueprint(authentication_bp)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = Config.SECRET_KEY
jwt = JWTManager(app)
app.config["JWT_ALGORITHM"] = Config.JWT_ALGORITHM

# Setting up the Database
app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
db.create_all()

# Main app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
