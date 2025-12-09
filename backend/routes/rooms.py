from flask import request, jsonify
from datetime import datetime
from models import db, Room, CurrentStatus
from routes import api_bp

@api_bp.route('/rooms', methods=['GET'])
def get_rooms():
    """모든 강의실 목록 조회 (상태 정보 포함)"""
    rooms = Room.query.all()
    result = []
    
    for room in rooms:
        room_data = room.to_dict()
        # 현재 상태 정보 추가
        if room.current_status:
            room_data['status'] = room.current_status.to_dict()
        else:
            # 기본 상태 생성
            default_status = CurrentStatus(
                room_id=room.id,
                rssi=None,
                status='vacant'
            )
            db.session.add(default_status)
            db.session.commit()
            room_data['status'] = default_status.to_dict()
        
        result.append(room_data)
    
    return jsonify(result), 200

@api_bp.route('/rooms/<int:room_id>', methods=['GET'])
def get_room(room_id):
    """특정 강의실 조회 (상태 정보 포함)"""
    room = Room.query.get_or_404(room_id)
    room_data = room.to_dict()
    
    # 현재 상태 정보 추가
    if room.current_status:
        room_data['status'] = room.current_status.to_dict()
    else:
        # 기본 상태 생성
        default_status = CurrentStatus(
            room_id=room.id,
            rssi=None,
            status='vacant'
        )
        db.session.add(default_status)
        db.session.commit()
        room_data['status'] = default_status.to_dict()
    
    return jsonify(room_data), 200

@api_bp.route('/rooms/<int:room_id>/threshold', methods=['PUT'])
def update_room_threshold(room_id):
    """강의실 임계값 설정"""
    room = Room.query.get_or_404(room_id)
    data = request.get_json()
    
    if 'threshold' in data:
        room.threshold = data['threshold']
        db.session.commit()
    
    return jsonify({
        'roomId': room.id,
        'threshold': room.threshold
    }), 200
