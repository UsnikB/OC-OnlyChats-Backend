from datetime import datetime
from database import db

class Meeting(db.Model):
    __tablename__ = 'meeting'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    scheduled_at = db.Column(db.DateTime)
    participants = db.relationship('MeetingParticipant', backref='meeting', lazy=True)

    def __init__(self, title, participants, scheduled_at):
        self.title = title
        self.created_at = datetime.utcnow()
        self.scheduled_at = scheduled_at
        self.participants = []
        for participant in participants:
            self.participants.append(MeetingParticipant(username=participant, meeting=self))
        db.session.add(self)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'created_at': self.created_at.isoformat(),
            'scheduled_at': self.scheduled_at.isoformat(),
            'participants': [p.username for p in self.participants]
        }

class MeetingParticipant(db.Model):
    __tablename__ = 'meeting_participant'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    meeting_id = db.Column(db.Integer, db.ForeignKey('meeting.id'), nullable=False)

    def __init__(self, username, meeting):
        self.username = username
        self.meeting = meeting

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'created_at': self.created_at.isoformat(),
            'meeting_id': self.meeting_id
        }