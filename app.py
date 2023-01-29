from flask import Flask
from routes.routes import routes_bp, authentication_bp
from flask_jwt_extended import JWTManager
from auth.authentication import create_token, decode_token

app = Flask(__name__)
app.register_blueprint(routes_bp)
app.register_blueprint(authentication_bp)

jwt = JWTManager(app)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
