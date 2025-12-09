# Flask 백엔드와 Next.js 프론트엔드 연결 가이드

## 현재 상태

✅ **백엔드 (Flask)**: `http://localhost:5000`에서 실행
✅ **프론트엔드 (Next.js)**: `http://localhost:3000`에서 실행
✅ **API 클라이언트**: `frontend/src/utils/api.ts` 생성 완료
✅ **CORS 설정**: 백엔드에서 모든 origin 허용

## 연결 설정 방법

### 1. 환경 변수 설정

프론트엔드 디렉토리에 `.env.local` 파일을 생성하세요:

```bash
cd frontend
cp env.example .env.local
```

`.env.local` 파일 내용:
```
NEXT_PUBLIC_API_URL=http://localhost:5000
```

### 2. 백엔드 서버 실행

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 데이터베이스 초기화 (최초 1회)
python init_db.py

# 서버 실행
python app.py
```

백엔드는 `http://localhost:5000`에서 실행됩니다.

### 3. 프론트엔드 서버 실행

```bash
cd frontend
npm install
npm run dev
```

프론트엔드는 `http://localhost:3000`에서 실행됩니다.

## API 연결 확인

### 백엔드 헬스 체크

```bash
curl http://localhost:5000/
curl http://localhost:5000/api/health
```

### 프론트엔드에서 API 호출

프론트엔드 코드에서 API를 사용하는 방법:

```typescript
import { dashboardApi, roomsApi, systemApi } from '@/utils/api';

// 대시보드 데이터 가져오기
const response = await dashboardApi.getData();
if (response.data) {
  console.log(response.data.rooms);
}

// 강의실 목록 가져오기
const roomsResponse = await roomsApi.getAll();

// 시스템 상태 가져오기
const systemResponse = await systemApi.getStatus();
```

## 현재 연결된 페이지

- ✅ **대시보드** (`/dashboard`): 백엔드 API와 연결됨
- ⚠️ **나머지 페이지들**: 아직 mock 데이터 사용 중 (필요시 연결 가능)

## API 엔드포인트

### 백엔드 API

```
GET  /                     # 서버 상태
GET  /api/health           # DB 헬스 체크
GET  /api/rooms            # 모든 강의실 목록
GET  /api/rooms/<id>       # 특정 강의실 조회
PUT  /api/rooms/<id>/threshold  # 강의실 임계값 설정
POST /api/beacon           # 비콘 데이터 수신
POST /api/heartbeat        # 스캐너/서버 하트비트
GET  /api/system           # 시스템 상태 조회
GET  /api/dashboard        # 대시보드 데이터
```

## 문제 해결

### CORS 오류가 발생하는 경우

백엔드 `app.py`에서 CORS 설정 확인:
```python
CORS(app, resources={r"/api/*": {"origins": "*"}})
```

### API 연결이 안 되는 경우

1. 백엔드 서버가 실행 중인지 확인
2. `.env.local` 파일의 `NEXT_PUBLIC_API_URL` 확인
3. 브라우저 개발자 도구의 Network 탭에서 요청 확인

### 데이터가 표시되지 않는 경우

1. 데이터베이스에 샘플 데이터가 있는지 확인:
   ```bash
   cd backend
   python init_db.py
   ```

2. 백엔드 API가 정상 응답하는지 확인:
   ```bash
   curl http://localhost:5000/api/rooms
   ```

## 다음 단계

다른 페이지들도 백엔드 API와 연결하려면:

1. 해당 페이지에서 `@/utils/api`의 함수 사용
2. mock 데이터 대신 API 응답 사용
3. 로딩 상태 및 에러 처리 추가


