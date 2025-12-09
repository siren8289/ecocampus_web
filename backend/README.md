# EcoCampus Backend API

Flask와 PostgreSQL을 사용한 실시간 강의실 점유 모니터링 시스템의 백엔드 API입니다.

## 기술 스택

- **Flask**: Python 웹 프레임워크
- **PostgreSQL**: 관계형 데이터베이스
- **SQLAlchemy**: ORM
- **Flask-Migrate**: 데이터베이스 마이그레이션

## API 엔드포인트

```
GET  /                     # 서버 상태
GET  /api/health           # DB 헬스 체크

🏫 Rooms
├── GET  /api/rooms                    # 모든 강의실 목록
├── GET  /api/rooms/<id>                # 특정 강의실 조회
└── PUT  /api/rooms/<id>/threshold     # 강의실 임계값 설정

📡 Beacon Scanner
└── POST /api/beacon                    # 비콘 데이터 수신

⚙️ System
├── POST /api/heartbeat                 # 스캐너 하트비트
└── GET  /api/system                    # 시스템 상태 조회

📊 Dashboard
└── GET  /api/dashboard                 # 대시보드 데이터
```

## 설치 및 설정

### 1. 가상 환경 생성 및 활성화

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. 의존성 설치

```bash
pip install -r requirements.txt
```

### 3. PostgreSQL 데이터베이스 생성

```bash
# PostgreSQL에 접속
psql -U postgres

# 데이터베이스 생성
CREATE DATABASE ecocampus;
```

### 4. 환경 변수 설정

`env.example` 파일을 복사하여 `.env` 파일을 생성하고 필요한 값들을 설정하세요:

```bash
cp env.example .env
```

`.env` 파일을 열어서 데이터베이스 연결 정보를 수정하세요:

```
DATABASE_URL=postgresql://postgres:your_password@localhost:5432/ecocampus
```

### 5. 데이터베이스 초기화

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

또는 샘플 데이터와 함께 초기화:

```bash
python init_db.py
```

### 6. 서버 실행

```bash
python app.py
```

서버는 `http://localhost:5000`에서 실행됩니다.

## API 사용 예시

### 서버 상태 확인

```bash
curl http://localhost:5000/
```

### DB 헬스 체크

```bash
curl http://localhost:5000/api/health
```

### 강의실 목록 조회

```bash
curl http://localhost:5000/api/rooms
```

### 특정 강의실 조회

```bash
curl http://localhost:5000/api/rooms/room-1
```

### 강의실 임계값 설정

```bash
curl -X PUT http://localhost:5000/api/rooms/room-1/threshold \
  -H "Content-Type: application/json" \
  -d '{
    "rssiThreshold": -70.0,
    "occupancyThreshold": 0.9
  }'
```

### 비콘 데이터 수신

```bash
curl -X POST http://localhost:5000/api/beacon \
  -H "Content-Type: application/json" \
  -d '{
    "roomId": "room-1",
    "uuid": "FDA50693-A4E2-4FB1-AFCF-C6EB07647825",
    "major": 1,
    "minor": 1,
    "rssi": -65.0,
    "battery": 85
  }'
```

### 스캐너 하트비트

```bash
curl -X POST http://localhost:5000/api/heartbeat \
  -H "Content-Type: application/json" \
  -d '{
    "scannerId": "scanner-1",
    "name": "라즈베리파이 #1",
    "location": "A동 1층",
    "status": "online",
    "ipAddress": "192.168.1.100"
  }'
```

### 시스템 상태 조회

```bash
curl http://localhost:5000/api/system
```

### 대시보드 데이터 조회

```bash
curl http://localhost:5000/api/dashboard
```

## 데이터 모델

### Room (강의실)
- id, name, building, capacity
- current_occupancy, status, rssi
- last_update, created_at

### Beacon (비콘)
- id, room_id, uuid, major, minor
- rssi, battery, last_seen

### EventLog (이벤트 로그)
- id, room_id, timestamp, rssi
- occupied, message

### Scanner (스캐너)
- id, name, location, status
- ip_address, last_ping

### SystemStatus (시스템 상태)
- id, timestamp, cpu_usage
- memory_usage, disk_usage, server_status

### Threshold (임계값)
- id, room_id, rssi_threshold
- occupancy_threshold

## 개발

### 데이터베이스 마이그레이션

모델 변경 후:

```bash
flask db migrate -m "Description of changes"
flask db upgrade
```

## 배포

프로덕션 환경에서는:

1. `.env` 파일에서 `FLASK_ENV=production` 설정
2. `SECRET_KEY`를 안전한 랜덤 값으로 변경
3. 데이터베이스 연결 정보 확인
4. Gunicorn 등 WSGI 서버 사용 권장

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```
