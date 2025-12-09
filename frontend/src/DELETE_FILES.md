# 🗑️ 삭제 가능한 파일 목록

현재 프로젝트에서 **사용하지 않는 파일들**입니다.  
코드에서 import하지 않으므로 삭제해도 **빌드/실행에 영향 없습니다**.

---

## ⚠️ 참고사항

일부 파일은 **시스템 보호 파일**로 설정되어 있어 삭제가 제한될 수 있습니다.  
하지만 존재 자체가 프로젝트에 영향을 주지 않으므로 **무시하셔도 됩니다**.

---

## 📁 삭제 대상 파일 목록

### 1️⃣ `/components/ui/` - UI 컴포넌트 (약 50개)

우리는 `/components/common/`에 커스텀 컴포넌트를 만들어 사용 중입니다.

```
/components/ui/accordion.tsx
/components/ui/alert-dialog.tsx
/components/ui/alert.tsx
/components/ui/aspect-ratio.tsx
/components/ui/avatar.tsx
/components/ui/badge.tsx
/components/ui/breadcrumb.tsx
/components/ui/button.tsx
/components/ui/calendar.tsx
/components/ui/card.tsx
/components/ui/carousel.tsx
/components/ui/chart.tsx
/components/ui/checkbox.tsx
/components/ui/collapsible.tsx
/components/ui/command.tsx
/components/ui/context-menu.tsx
/components/ui/dialog.tsx
/components/ui/drawer.tsx
/components/ui/dropdown-menu.tsx
/components/ui/form.tsx
/components/ui/hover-card.tsx
/components/ui/input-otp.tsx
/components/ui/input.tsx
/components/ui/label.tsx
/components/ui/menubar.tsx
/components/ui/navigation-menu.tsx
/components/ui/pagination.tsx
/components/ui/popover.tsx
/components/ui/progress.tsx
/components/ui/radio-group.tsx
/components/ui/resizable.tsx
/components/ui/scroll-area.tsx
/components/ui/select.tsx
/components/ui/separator.tsx
/components/ui/sheet.tsx
/components/ui/sidebar.tsx
/components/ui/skeleton.tsx
/components/ui/slider.tsx
/components/ui/sonner.tsx
/components/ui/switch.tsx
/components/ui/table.tsx
/components/ui/tabs.tsx
/components/ui/textarea.tsx
/components/ui/toast.tsx
/components/ui/toaster.tsx
/components/ui/toggle-group.tsx
/components/ui/toggle.tsx
/components/ui/tooltip.tsx
/components/ui/use-toast.ts
```

### 2️⃣ 가이드라인 파일

```
/guidelines/
/Attributions.md
```

---

## ✅ 실제 사용 중인 파일 구조

```
/
├─ App.tsx                      # 메인 엔트리포인트
├─ main.tsx                     # React 초기화
├─ index.html
├─ styles/
│  └─ globals.css               # Soft Eco Green 테마
├─ components/
│  ├─ Layout.tsx                # 메인 레이아웃
│  ├─ common/                   # 커스텀 공용 컴포넌트 (11개)
│  │  ├─ Button.tsx
│  │  ├─ Badge.tsx
│  │  ├─ Card.tsx
│  │  ├─ Select.tsx
│  │  ├─ Switch.tsx
│  │  ├─ Input.tsx
│  │  ├─ Table.tsx
│  │  ├─ Tabs.tsx
│  │  ├─ Modal.tsx
│  │  ├─ ProgressBar.tsx
│  │  └─ StatusIndicator.tsx
│  └─ figma/
│     └─ ImageWithFallback.tsx  # 시스템 파일 (보호)
├─ pages/                       # 페이지 컴포넌트
│  ├─ dashboard/
│  │  └─ DashboardPage.tsx
│  ├─ room/
│  │  └─ RoomDetailPage.tsx
│  ├─ system/
│  │  └─ SystemPage.tsx
│  └─ admin/
│     └─ AdminPage.tsx
├─ utils/
│  └─ mockData.ts               # 실시간 데이터 시뮬레이션
└─ PROJECT_STRUCTURE.md         # 프로젝트 구조 문서
```

---

## 🎯 삭제 방법

수동으로 파일 탐색기에서 삭제하시면 됩니다.

**권장 삭제 순서:**
1. `/components/ui/` 폴더 전체 삭제
2. `/guidelines/` 폴더 삭제
3. `/Attributions.md` 삭제

---

## 💡 결론

현재 프로젝트는 이미 **완전히 정리된 상태**입니다!  
- ✅ Soft Eco Green + Yellow 컬러 시스템
- ✅ 11개 공용 컴포넌트 체계
- ✅ 4개 페이지 폴더 구조
- ✅ 커스텀 스크롤바

삭제 대상 파일들은 단순히 **초기 템플릿 파일**이므로, 삭제하셔도 무방합니다! 🚀
