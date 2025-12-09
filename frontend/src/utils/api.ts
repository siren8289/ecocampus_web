/**
 * API 클라이언트 유틸리티
 */

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:5000';

export interface ApiResponse<T> {
  data?: T;
  error?: string;
  success?: boolean;
}

/**
 * API 요청 헬퍼 함수
 */
async function apiRequest<T>(
  endpoint: string,
  options: RequestInit = {}
): Promise<ApiResponse<T>> {
  try {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      ...options,
    });

    if (!response.ok) {
      const error = await response.json().catch(() => ({ error: 'Unknown error' }));
      return { error: error.error || `HTTP ${response.status}` };
    }

    const data = await response.json();
    return { data, success: true };
  } catch (error) {
    return { error: error instanceof Error ? error.message : 'Network error' };
  }
}

/**
 * Rooms API
 */
export const roomsApi = {
  getAll: () => apiRequest<any[]>('/api/rooms'),
  getById: (id: number) => apiRequest<any>(`/api/rooms/${id}`),
  updateThreshold: (id: number, threshold: number) =>
    apiRequest(`/api/rooms/${id}/threshold`, {
      method: 'PUT',
      body: JSON.stringify({ threshold }),
    }),
};

/**
 * Beacon API
 */
export const beaconApi = {
  sendData: (data: {
    beaconMac: string;
    rssi: number;
    uuid?: string;
    major?: number;
    minor?: number;
  }) =>
    apiRequest('/api/beacon', {
      method: 'POST',
      body: JSON.stringify(data),
    }),
};

/**
 * System API
 */
export const systemApi = {
  getStatus: () => apiRequest<any>('/api/system'),
  sendHeartbeat: (source: 'scanner' | 'server', message?: string) =>
    apiRequest('/api/heartbeat', {
      method: 'POST',
      body: JSON.stringify({ source, message }),
    }),
};

/**
 * Dashboard API
 */
export const dashboardApi = {
  getData: () => apiRequest<any>('/api/dashboard'),
};

/**
 * Health Check API
 */
export const healthApi = {
  check: () => apiRequest<any>('/api/health'),
  serverStatus: () => apiRequest<any>('/'),
};


