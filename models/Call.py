from datetime import datetime

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
