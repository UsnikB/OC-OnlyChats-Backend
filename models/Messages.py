from app import db
from datetime import datetime

class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.String(500))
    sent_at = db.Column(db.DateTime, default=datetime.utcnow)
    read_at = db.Column(db.DateTime)

    def __init__(self, sender, receiver, content):
        self.sender_id = sender.id
        self.receiver_id = receiver.id
        self.content = content
        db.session.add(self)

    def mark_as_read(self):
        self.read_at = datetime.utcnow()

    def to_dict(self):
        return {
            'id': self.id,
            'sender': self.sender_id,
            'receiver': self.receiver_id,
            'content': self.content,
            'sent_at': self.sent_at.isoformat(),
            'read_at': self.read_at.isoformat() if self.read_at else None
        }