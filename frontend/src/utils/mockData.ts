export interface Room {
  id: string;
  name: string;
  building: string;
  capacity: number;
  currentOccupancy: number;
  status: 'available' | 'occupied' | 'full';
  rssi?: number;
  lastUpdate?: Date;
  currentClass?: string;
  nextClass?: string;
  nextClassTime?: string;
}

export interface RSSIDataPoint {
  time: string;
  beacon1: number;
  beacon2: number;
  beacon3: number;
}

export interface EventLog {
  id: string;
  timestamp: Date;
  type: 'enter' | 'exit' | 'threshold' | 'system';
  message: string;
}

export interface RoomEvent {
  id: string;
  timestamp: Date;
  rssi: number;
  occupied: boolean;
}

export interface Beacon {
  id: string;
  uuid: string;
  major: number;
  minor: number;
  rssi: number;
  battery: number;
  lastSeen: Date;
}

export function generateMockRooms(): Room[] {
  const buildings = ['A동', 'B동', 'C동', 'D동'];
  const rooms: Room[] = [];
  const classes = ['데이터구조', '알고리즘', '운영체제', '데이터베이스', '네트워크', '소프트웨어공학', '인공지능', '컴퓨터그래픽스'];
  
  for (let i = 1; i <= 24; i++) {
    const capacity = [30, 50, 80, 100, 150][Math.floor(Math.random() * 5)];
    const currentOccupancy = Math.floor(Math.random() * (capacity + 10));
    const actualOccupancy = Math.min(currentOccupancy, capacity);
    
    let status: 'available' | 'occupied' | 'full';
    if (actualOccupancy === 0) status = 'available';
    else if (actualOccupancy >= capacity * 0.9) status = 'full';
    else status = 'occupied';
    
    rooms.push({
      id: `room-${i}`,
      name: `${Math.floor((i - 1) / 6) + 1}0${((i - 1) % 6) + 1}호`,
      building: buildings[Math.floor((i - 1) / 6) % 4],
      capacity,
      currentOccupancy: actualOccupancy,
      status,
      rssi: -50 + Math.floor(Math.random() * 40),
      lastUpdate: new Date(Date.now() - Math.floor(Math.random() * 120000)),
      currentClass: status !== 'available' ? classes[Math.floor(Math.random() * classes.length)] : undefined,
      nextClass: Math.random() > 0.5 ? classes[Math.floor(Math.random() * classes.length)] : undefined,
      nextClassTime: Math.random() > 0.5 ? `${14 + Math.floor(Math.random() * 4)}:00` : undefined,
    });
  }
  
  return rooms;
}

export function generateRSSIData(): RSSIDataPoint[] {
  const data: RSSIDataPoint[] = [];
  const now = new Date();
  
  for (let i = 30; i >= 0; i--) {
    const time = new Date(now.getTime() - i * 2000);
    data.push({
      time: time.toLocaleTimeString('ko-KR'),
      beacon1: -60 + Math.random() * 20,
      beacon2: -70 + Math.random() * 20,
      beacon3: -55 + Math.random() * 25,
    });
  }
  
  return data;
}

export function generateEventLogs(): EventLog[] {
  const events: EventLog[] = [];
  const now = Date.now();
  const types: EventLog['type'][] = ['enter', 'exit', 'threshold', 'system'];
  const messages = {
    enter: ['사용자가 입장했습니다', '비콘 신호 감지됨'],
    exit: ['사용자가 퇴장했습니다', '비콘 신호 사라짐'],
    threshold: ['RSSI 임계값 초과', '점유 인원 경고'],
    system: ['시스템 정상 작동 중', '스캐너 연결 확인됨'],
  };
  
  for (let i = 0; i < 20; i++) {
    const type = types[Math.floor(Math.random() * types.length)];
    const messageList = messages[type];
    
    events.push({
      id: `event-${i}`,
      timestamp: new Date(now - i * 60000),
      type,
      message: messageList[Math.floor(Math.random() * messageList.length)],
    });
  }
  
  return events.sort((a, b) => b.timestamp.getTime() - a.timestamp.getTime());
}

export function generateRoomEventLogs(): RoomEvent[] {
  const events: RoomEvent[] = [];
  const now = Date.now();
  
  for (let i = 0; i < 20; i++) {
    events.push({
      id: `event-${i}`,
      timestamp: new Date(now - i * 60000),
      rssi: -50 + Math.random() * 40,
      occupied: Math.random() > 0.5,
    });
  }
  
  return events;
}