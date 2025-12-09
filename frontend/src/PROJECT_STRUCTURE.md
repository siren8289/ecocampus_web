# 프로젝트 구조 (Project Structure)

## 📁 실제 사용 중인 폴더 구조

```
/
├── App.tsx                         # 메인 앱 (라우터 설정)
│
├── components/                     # 컴포넌트 폴더
│   ├── Layout.tsx                  # 공용 레이아웃 (사이드바 포함)
│   │
│   └── common/                     # ✅ 공용 UI 컴포넌트 (실제 사용)
│       ├── Badge.tsx               # 뱃지 컴포넌트
│       ├── Button.tsx              # 버튼 컴포넌트
│       ├── Card.tsx                # 카드 컴포넌트
│       ├── EmptyState.tsx          # 빈 상태 표시
│       ├── IconButton.tsx          # 아이콘 버튼
│       ├── InfoBox.tsx             # 정보 박스
│       ├── Input.tsx               # 입력 필드
│       ├── SearchInput.tsx         # 검색 입력
│       ├── StatCard.tsx            # 통계 카드
│       ├── StatusCard.tsx          # 상태 카드
│       └── Table.tsx               # 테이블 컴포넌트
│
├── pages/                          # 페이지 폴더
│   │
│   ├── dashboard/                  # 대시보드 페이지
│   │   ├── Dashboard.tsx           # 메인 페이지 컴포넌트
│   │   └── components/             # 대시보드 전용 컴포넌트
│   │       ├── RoomCard.tsx        # 강의실 카드
│   │       └── SystemStatusPanel.tsx # 시스템 상태 패널
│   │
│   ├── room-detail/                # 강의실 상세 페이지
│   │   ├── RoomDetail.tsx          # 메인 페이지 컴포넌트
│   │   └── components/             # 강의실 상세 전용 컴포넌트
│   │       ├── BeaconInfoPanel.tsx # 비콘 정보 패널
│   │       ├── EventLogTable.tsx   # 이벤트 로그 테이블
│   │       ├── RSSIGraph.tsx       # RSSI 그래프
│   │       └── ThresholdSettings.tsx # 임계값 설정
│   │
│   ├── system-monitor/             # 시스템 모니터 페이지
│   │   ├── SystemMonitor.tsx       # 메인 페이지 컴포넌트
│   │   └── components/             # 시스템 모니터 전용 컴포넌트
│   │       ├── BeaconListTable.tsx # 비콘 목록 테이블
│   │       ├── ScannerStatusList.tsx # 스캐너 상태 목록
│   │       └── SystemStatusPanel.tsx # 시스템 상태 패널
│   │
│   ├── admin-settings/             # 관리자 설정 페이지
│   │   ├── AdminSettings.tsx       # 메인 페이지 컴포넌트
│   │   └── components/             # 관리자 설정 전용 컴포넌트
│   │       ├── RoomManagement.tsx  # 강의실 관리
│   │       ├── ThresholdManagement.tsx # 임계값 관리
│   │       └── UserPermission.tsx  # 사용자 권한 관리
│   │
│   └── not-found/                  # 404 페이지
│       └── NotFound.tsx            # 404 페이지 컴포넌트
│
├── utils/                          # 유틸리티 폴더
│   └── mockData.ts                 # 목 데이터 생성
│
└── styles/                         # 스타일 폴더
    └── globals.css                 # 전역 CSS (Tailwind)
```

---

## ⚠️ 무시해야 할 폴더 (시스템 파일, 사용 안 함)

```
components/
├── ui/                             # ❌ shadcn/ui 기본 파일들 (사용 안 함)
│   └── ... (50개 이상의 파일)      # 시스템 보호 파일이라 삭제 불가
│
└── figma/                          # ❌ Figma 관련 (사용 안 함)
    └── ImageWithFallback.tsx       # 시스템 보호 파일이라 삭제 불가
```

---

## 🎯 주요 페이지 라우팅

| 경로 | 파일 | 설명 |
|------|------|------|
| `/dashboard` | `/pages/dashboard/Dashboard.tsx` | 대시보드 (강의실 점유 현황) |
| `/room/:id` | `/pages/room-detail/RoomDetail.tsx` | 강의실 상세 정보 |
| `/system` | `/pages/system-monitor/SystemMonitor.tsx` | 시스템 모니터링 |
| `/admin` | `/pages/admin-settings/AdminSettings.tsx` | 관리자 설정 |
| `*` | `/pages/not-found/NotFound.tsx` | 404 페이지 |

---

## 🧩 공용 컴포넌트 사용법

### Button
```tsx
import { Button } from '../../components/common/Button';

<Button variant="primary" size="md" onClick={handleClick}>
  클릭
</Button>
```

### Card
```tsx
import { Card, CardHeader, CardTitle } from '../../components/common/Card';

<Card>
  <CardHeader>
    <CardTitle>제목</CardTitle>
  </CardHeader>
  내용
</Card>
```

### Table
```tsx
import { Table, TableHeader, TableBody, TableRow, TableHead, TableCell } 
  from '../../components/common/Table';

<Table>
  <TableHeader>
    <TableRow>
      <TableHead>헤더</TableHead>
    </TableRow>
  </TableHeader>
  <TableBody>
    <TableRow>
      <TableCell>내용</TableCell>
    </TableRow>
  </TableBody>
</Table>
```

### Badge
```tsx
import { Badge } from '../../components/common/Badge';

<Badge variant="success">사용 가능</Badge>
<Badge variant="warning">주의</Badge>
<Badge variant="danger">사용 중</Badge>
```

---

## 📝 컴포넌트 작성 규칙

1. **페이지별 전용 컴포넌트**: `/pages/{페이지}/components/` 폴더에 배치
2. **공용 컴포넌트**: `/components/common/` 폴더에 배치
3. **Import 경로**: 상대 경로 사용 (`../../../components/common/Button`)
4. **한국어 사용**: 모든 UI 텍스트는 한국어로 작성
5. **Tailwind CSS**: 스타일링은 Tailwind 클래스 사용

---

## 🚀 기술 스택

- **React 18** + **TypeScript**
- **React Router** (페이지 라우팅)
- **Tailwind CSS** (스타일링)
- **Recharts** (RSSI 그래프)
- **Lucide React** (아이콘)
- **Vite** (빌드 도구)

---

## 📌 주요 기능

1. **실시간 강의실 점유 모니터링** (RSSI 기반)
2. **강의실별 상세 정보** (RSSI 그래프, 비콘 정보, 이벤트 로그)
3. **시스템 상태 모니터링** (스캐너, 서버, DB 상태)
4. **관리자 설정** (강의실 관리, 임계값 설정, 사용자 권한)

---

## ✅ 정리 완료 사항

- ✅ 페이지별 폴더 구조로 재정리
- ✅ 공용 UI 컴포넌트를 `/components/common/`으로 통일
- ✅ 중복 코드 제거
- ✅ 일관된 import 경로 사용
- ✅ 한국어 UI 통일

---

**참고**: `/components/ui/`와 `/components/figma/` 폴더는 시스템 보호 파일이라 삭제할 수 없지만, 실제로는 사용하지 않으므로 무시하시면 됩니다.
