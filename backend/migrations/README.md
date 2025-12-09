# 데이터베이스 마이그레이션

이 디렉토리는 Flask-Migrate가 자동으로 생성하는 마이그레이션 파일들을 저장합니다.

## 마이그레이션 명령어

### 초기화 (최초 1회만)
```bash
flask db init
```

### 마이그레이션 파일 생성
```bash
flask db migrate -m "Description of changes"
```

### 마이그레이션 적용
```bash
flask db upgrade
```

### 마이그레이션 롤백
```bash
flask db downgrade
```

### 마이그레이션 히스토리 확인
```bash
flask db history
```

### 현재 버전 확인
```bash
flask db current
```



