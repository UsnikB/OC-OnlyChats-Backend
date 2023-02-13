from app import db
from datetime import datetime

class Notification(db.Model):
    __tablename__ = 'notification'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, user_id, type, content, sender_id=None):
        self.user_id = user_id
        self.type = type
        self.content = content
        self.sender_id = sender_id
        db.session.add(self)