from datetime import datetime
from database import db
from models.UserType import UserType
from models.UserUserType import UserUserType

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)

    def __init__(self, username, email, password, user_type="customer"):
        self.username = username
        self.email = email
        self.password = password
        db.session.add(self)

        # Add user to user_user_type table with default customer type
        user_type_id = UserType.query.filter_by(name=user_type).first().id
        
        user_user_type = UserUserType(user_id=self.id, user_type_id=user_type_id)
        db.session.add(user_user_type)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'created_at': self.created_at.isoformat(),
            'last_login': self.last_login.isoformat() if self.last_login else None
        }
