from flask import Flask
from routes.routes import routes_bp
from routes.authentication import authentication_bp
from routes.users import users_bp
from flask_jwt_extended import JWTManager
from config import Config
from models import  Call, CallParticipant, Meeting, MeetingParticipant, Message, Notification, Room, RoomMember, User
from database import db

# Created the Flask app
app = Flask(__name__)

# Registering route Blueprint
app.register_blueprint(routes_bp)
app.register_blueprint(authentication_bp)
app.register_blueprint(users_bp)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = Config.SECRET_KEY
jwt = JWTManager(app)
app.config["JWT_ALGORITHM"] = Config.JWT_ALGORITHM

# Setting up the Database
app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Main app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')
