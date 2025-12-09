from flask import jsonify
from datetime import datetime
from models import db
from routes import api_bp

@api_bp.route('/health', methods=['GET'])
def health_check():
    """DB 헬스 체크"""
    try:
        # 데이터베이스 연결 테스트
        db.session.execute('SELECT 1')
        db_status = 'connected'
    except Exception as e:
        db_status = f'error: {str(e)}'
    
    return jsonify({
        'status': 'healthy',
        'database': db_status,
        'timestamp': datetime.utcnow().isoformat()
    }), 200

