from database import db
from datetime import datetime


class UserUserType(db.Model):
    __tablename__ = 'user_user_type'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    user_type_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, user_id, user_type_id):
        self.user_id = user_id
        self.user_type_id = user_type_id
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'user_type_id': self.user_type_id
        }
