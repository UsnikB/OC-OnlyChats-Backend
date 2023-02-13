from app import db
from datetime import datetime

class Room(db.Model):
    __tablename__ = 'room'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    members = db.relationship('RoomMember', backref='room', lazy=True)
    calls = db.relationship('Call', backref='room', lazy=True)

    def __init__(self, name):
        self.name = name
        db.session.add(self)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.isoformat()
        }

class RoomMember(db.Model):
    __tablename__ = 'room_member'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, user_id, room_id):
        self.user_id = user_id
        self.room_id = room_id
        db.session.add(self)

class Call(db.Model):
    __tablename__ = 'call'
    id = db.Column(db.Integer, primary_key=True)
    room_id = db.Column(db.Integer, db.ForeignKey('room.id'), nullable=False)
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    end_time = db.Column(db.DateTime)
    duration = db.Column(db.Integer)
    quality = db.Column(db.String(50))
    participants = db.relationship('CallParticipant', backref='call', lazy=True)

    def __init__(self, room_id):
        self.room_id = room_id
        db.session.add(self)

class CallParticipant(db.Model):
    __tablename__ = 'call_participant'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    call_id = db.Column(db.Integer, db.ForeignKey('call.id'), nullable=False)
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, user_id, call_id):
        self.user_id = user_id
        self.call_id = call_id
        db.session.add(self)
