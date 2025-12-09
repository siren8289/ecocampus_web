from flask import jsonify, request
from datetime import datetime, timedelta
from models import db, Room, CurrentStatus, BeaconHistory, SystemHeartbeat
from routes import api_bp

@api_bp.route('/dashboard', methods=['GET'])
def get_dashboard():
    """대시보드 데이터 조회"""
    try:
        # 모든 강의실 (상태 정보 포함)
        rooms = Room.query.all()
        rooms_data = []
        
        for room in rooms:
            room_data = room.to_dict()
            # 현재 상태 정보 추가
            if room.current_status:
                room_data['status'] = room.current_status.to_dict()
            else:
                # 기본 상태
                room_data['status'] = {
                    'roomId': room.id,
                    'rssi': None,
                    'status': 'vacant'
                }
            rooms_data.append(room_data)
        
        # 최근 하트비트 (최근 1시간)
        since = datetime.utcnow() - timedelta(hours=1)
        recent_heartbeats = SystemHeartbeat.query.filter(
            SystemHeartbeat.timestamp >= since
        ).order_by(SystemHeartbeat.timestamp.desc()).limit(100).all()
        
        # 타입별로 분류
        scanners = [h for h in recent_heartbeats if h.source == 'scanner']
        servers = [h for h in recent_heartbeats if h.source == 'server']
        
        # 최근 RSSI 히스토리 (최근 1시간, 최대 100개)
        hours = request.args.get('hours', 1, type=int)
        history_since = datetime.utcnow() - timedelta(hours=hours)
        recent_history = BeaconHistory.query.filter(
            BeaconHistory.timestamp >= history_since
        ).order_by(BeaconHistory.timestamp.desc()).limit(100).all()
        
        # 통계 계산
        total_rooms = len(rooms)
        occupied_rooms = 0
        vacant_rooms = 0
        
        for room in rooms:
            if room.current_status:
                if room.current_status.status == 'occupied':
                    occupied_rooms += 1
                else:
                    vacant_rooms += 1
        
        # 최근 하트비트에서 온라인 상태 확인
        online_scanners = len(set([h.source for h in scanners]))
        online_servers = len(set([h.source for h in servers]))
        
        return jsonify({
            'rooms': rooms_data,
            'statistics': {
                'totalRooms': total_rooms,
                'occupiedRooms': occupied_rooms,
                'vacantRooms': vacant_rooms,
                'onlineScanners': online_scanners,
                'onlineServers': online_servers
            },
            'recentHeartbeats': [h.to_dict() for h in recent_heartbeats[:20]],
            'recentHistory': [h.to_dict() for h in recent_history],
            'timestamp': datetime.utcnow().isoformat()
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
