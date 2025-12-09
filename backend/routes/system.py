from flask import request, jsonify
from datetime import datetime, timedelta
from models import db, SystemHeartbeat
from routes import api_bp

@api_bp.route('/heartbeat', methods=['POST'])
def heartbeat():
    """스캐너/서버 하트비트 수신"""
    data = request.get_json()
    
    try:
        source = data.get('source')  # 'scanner' or 'server'
        message = data.get('message', '')
        
        if not source:
            return jsonify({'error': 'source is required'}), 400
        
        if source not in ['scanner', 'server']:
            return jsonify({'error': "source must be 'scanner' or 'server'"}), 400
        
        # 하트비트 기록
        heartbeat = SystemHeartbeat(
            source=source,
            message=message
        )
        db.session.add(heartbeat)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'heartbeat': heartbeat.to_dict()
        }), 200
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@api_bp.route('/system', methods=['GET'])
def get_system_status():
    """시스템 상태 조회"""
    # 최근 하트비트 조회 (최근 1시간)
    since = datetime.utcnow() - timedelta(hours=1)
    recent_heartbeats = SystemHeartbeat.query.filter(
        SystemHeartbeat.timestamp >= since
    ).order_by(SystemHeartbeat.timestamp.desc()).all()
    
    # 타입별로 분류
    scanners = [h for h in recent_heartbeats if h.source == 'scanner']
    servers = [h for h in recent_heartbeats if h.source == 'server']
    
    # 최신 하트비트만 추출 (중복 제거)
    scanner_status = {}
    server_status = {}
    
    for hb in scanners:
        if hb.source not in scanner_status:
            scanner_status[hb.source] = hb.to_dict()
    
    for hb in servers:
        if hb.source not in server_status:
            server_status[hb.source] = hb.to_dict()
    
    return jsonify({
        'scanners': list(scanner_status.values()),
        'servers': list(server_status.values()),
        'recentHeartbeats': [h.to_dict() for h in recent_heartbeats[:50]],
        'timestamp': datetime.utcnow().isoformat()
    }), 200
