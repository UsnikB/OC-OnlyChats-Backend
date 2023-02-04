from flask import Flask
from routes.routes import routes_bp, authentication_bp
from flask_jwt_extended import JWTManager
from config import Config

app = Flask(__name__)
app.register_blueprint(routes_bp)
app.register_blueprint(authentication_bp)

jwt = JWTManager(app)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = Config.SECRET_KEY  # Change this!
jwt = JWTManager(app)
app.config["JWT_ALGORITHM"] = Config.JWT_ALGORITHM
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
