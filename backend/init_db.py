"""
데이터베이스 초기화 및 샘플 데이터 생성 스크립트
"""
from app import create_app
from models import db, Room, CurrentStatus, BeaconHistory, SystemHeartbeat
from datetime import datetime, timedelta

def init_database():
    app = create_app()
    
    with app.app_context():
        # 모든 테이블 삭제 후 재생성
        db.drop_all()
        db.create_all()
        
        # 샘플 강의실 데이터
        rooms = [
            Room(
                name='Room 101',
                beacon_mac='AA:BB:CC:DD:EE:01',
                uuid='FDA50693-A4E2-4FB1-AFCF-C6EB07647825',
                major=1,
                minor=1,
                threshold=-70
            ),
            Room(
                name='Room 102',
                beacon_mac='AA:BB:CC:DD:EE:02',
                uuid='FDA50693-A4E2-4FB1-AFCF-C6EB07647825',
                major=1,
                minor=2,
                threshold=-70
            ),
            Room(
                name='전산실',
                beacon_mac='AA:BB:CC:DD:EE:03',
                uuid='FDA50693-A4E2-4FB1-AFCF-C6EB07647825',
                major=2,
                minor=1,
                threshold=-65
            ),
            Room(
                name='강의실 201',
                beacon_mac='AA:BB:CC:DD:EE:04',
                uuid='FDA50693-A4E2-4FB1-AFCF-C6EB07647825',
                major=2,
                minor=2,
                threshold=-70
            ),
            Room(
                name='세미나실',
                beacon_mac='AA:BB:CC:DD:EE:05',
                threshold=-75
            ),
        ]
        
        for room in rooms:
            db.session.add(room)
        
        db.session.flush()  # ID 생성
        
        # 강의실별 현재 상태 생성
        statuses = [
            CurrentStatus(room_id=rooms[0].id, rssi=-65, status='occupied'),
            CurrentStatus(room_id=rooms[1].id, rssi=-75, status='vacant'),
            CurrentStatus(room_id=rooms[2].id, rssi=-60, status='occupied'),
            CurrentStatus(room_id=rooms[3].id, rssi=-72, status='vacant'),
            CurrentStatus(room_id=rooms[4].id, rssi=-80, status='vacant'),
        ]
        
        for status in statuses:
            db.session.add(status)
        
        # 샘플 RSSI 히스토리 데이터 (최근 1시간)
        now = datetime.utcnow()
        history_data = []
        
        for i in range(50):
            timestamp = now - timedelta(minutes=i*2)
            room = rooms[i % len(rooms)]
            rssi = -60 - (i % 30)
            status = 'occupied' if rssi > room.threshold else 'vacant'
            
            history_data.append(BeaconHistory(
                room_id=room.id,
                rssi=rssi,
                status=status,
                timestamp=timestamp
            ))
        
        for history in history_data:
            db.session.add(history)
        
        # 샘플 하트비트 데이터
        heartbeats = [
            SystemHeartbeat(
                source='scanner',
                message='라즈베리파이 #1 정상 작동'
            ),
            SystemHeartbeat(
                source='scanner',
                message='라즈베리파이 #2 정상 작동'
            ),
            SystemHeartbeat(
                source='server',
                message='메인 서버 정상 작동'
            ),
        ]
        
        for heartbeat in heartbeats:
            db.session.add(heartbeat)
        
        db.session.commit()
        print("✅ 데이터베이스 초기화 완료!")
        print(f"   - 강의실: {len(rooms)}개")
        print(f"   - 현재 상태: {len(statuses)}개")
        print(f"   - RSSI 히스토리: {len(history_data)}개")
        print(f"   - 하트비트: {len(heartbeats)}개")

if __name__ == '__main__':
    init_database()
