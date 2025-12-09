from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from dotenv import load_dotenv
from datetime import datetime

# 환경 변수 로드
load_dotenv()

from config import Config
from models import db
from routes import api_bp

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # CORS 설정
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # 데이터베이스 초기화
    db.init_app(app)
    migrate = Migrate(app, db)
    
    # Blueprint 등록
    app.register_blueprint(api_bp, url_prefix='/api')
    
    # 루트 엔드포인트 - 서버 상태
    @app.route('/', methods=['GET'])
    def server_status():
        return jsonify({
            'status': 'online',
            'message': 'EcoCampus API Server',
            'timestamp': datetime.utcnow().isoformat()
        }), 200
    
    # 데이터베이스 테이블 생성
    with app.app_context():
        db.create_all()
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
