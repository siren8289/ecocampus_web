from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Room(db.Model):
    """강의실 기본 정보"""
    __tablename__ = 'rooms'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    beacon_mac = db.Column(db.String(20), unique=True, nullable=False)
    uuid = db.Column(db.String(50), nullable=True)
    major = db.Column(db.Integer, nullable=True)
    minor = db.Column(db.Integer, nullable=True)
    threshold = db.Column(db.Integer, default=-70)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # 관계
    current_status = db.relationship('CurrentStatus', backref='room', uselist=False, cascade='all, delete-orphan')
    beacon_history = db.relationship('BeaconHistory', backref='room', lazy=True, cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'beaconMac': self.beacon_mac,
            'uuid': self.uuid,
            'major': self.major,
            'minor': self.minor,
            'threshold': self.threshold,
            'createdAt': self.created_at.isoformat() if self.created_at else None,
        }

class BeaconHistory(db.Model):
    """RSSI 로그 기록"""
    __tablename__ = 'beacon_history'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)
    rssi = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(20), nullable=False)  # occupied / vacant
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, index=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'roomId': self.room_id,
            'rssi': self.rssi,
            'status': self.status,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None,
        }

class CurrentStatus(db.Model):
    """각 강의실의 최신 상태"""
    __tablename__ = 'current_status'
    
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), primary_key=True)
    rssi = db.Column(db.Integer, nullable=True)
    status = db.Column(db.String(20), nullable=True)  # occupied / vacant
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'roomId': self.room_id,
            'rssi': self.rssi,
            'status': self.status,
            'updatedAt': self.updated_at.isoformat() if self.updated_at else None,
        }

class SystemHeartbeat(db.Model):
    """라즈베리파이 / 서버 모니터링"""
    __tablename__ = 'system_heartbeat'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    source = db.Column(db.String(20), nullable=False)  # 'scanner' or 'server'
    message = db.Column(db.String(100), nullable=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'source': self.source,
            'message': self.message,
            'timestamp': self.timestamp.isoformat() if self.timestamp else None,
        }
