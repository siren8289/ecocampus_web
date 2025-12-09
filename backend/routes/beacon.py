from flask import request, jsonify
from datetime import datetime
from models import db, Room, BeaconHistory, CurrentStatus
from routes import api_bp

@api_bp.route('/beacon', methods=['POST'])
def receive_beacon_data():
    """비콘 스캐너로부터 데이터 수신"""
    data = request.get_json()
    
    try:
        # 필수 필드 확인
        beacon_mac = data.get('beaconMac')
        rssi = data.get('rssi')
        
        if not beacon_mac or rssi is None:
            return jsonify({
                'error': 'Missing required fields: beaconMac, rssi'
            }), 400
        
        # 비콘 MAC으로 강의실 찾기
        room = Room.query.filter_by(beacon_mac=beacon_mac).first()
        
        if not room:
            return jsonify({
                'error': f'Room with beacon MAC {beacon_mac} not found'
            }), 404
        
        # RSSI와 threshold 비교하여 상태 결정
        status = 'occupied' if rssi > room.threshold else 'vacant'
        
        # RSSI 히스토리 기록
        beacon_history = BeaconHistory(
            room_id=room.id,
            rssi=rssi,
            status=status
        )
        db.session.add(beacon_history)
        
        # 현재 상태 조회 또는 생성
        current_status = CurrentStatus.query.get(room.id)
        
        if not current_status:
            current_status = CurrentStatus(room_id=room.id)
            db.session.add(current_status)
        
        # 현재 상태 업데이트
        current_status.rssi = rssi
        current_status.status = status
        current_status.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        return jsonify({
            'success': True,
            'room': room.to_dict(),
            'status': current_status.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'error': str(e)
        }), 500
