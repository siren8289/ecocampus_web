'use client';

import { ReactNode, useState } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { LayoutDashboard, Radio, Settings, Monitor, Menu, X } from 'lucide-react';

interface LayoutProps {
  children: ReactNode;
}

export function Layout({ children }: LayoutProps) {
  const pathname = usePathname();
  const [sidebarOpen, setSidebarOpen] = useState(true);

  const navItems = [
    { path: '/dashboard', icon: LayoutDashboard, label: '대시보드' },
    { path: '/system', icon: Monitor, label: '시스템 모니터' },
    { path: '/admin', icon: Settings, label: '관리자 설정' },
  ];

  // Check if current path is active or starts with the nav path
  const isPathActive = (path: string) => {
    if (path === '/dashboard') {
      return pathname === '/' || pathname === '/dashboard';
    }
    return pathname?.startsWith(path) ?? false;
  };

  return (
    <div className="h-screen flex overflow-hidden" style={{ background: '#FFFBF0' }}>
      {/* Sidebar */}
      <aside
        className={`bg-white border-r border-gray-200 transition-all duration-300 flex-shrink-0 ${
          sidebarOpen ? 'w-64' : 'w-20'
        }`}
      >
        <div className="h-full flex flex-col">
          {/* Logo */}
          <div className={`p-4 border-b border-gray-200 flex items-center ${
            sidebarOpen ? 'justify-between' : 'justify-center'
          }`}>
            {sidebarOpen && (
              <div className="flex items-center gap-2">
                <Radio className="w-6 h-6 text-[#81D18A]" />
                <span className="text-gray-900">강의실 모니터</span>
              </div>
            )}
            {!sidebarOpen && (
              <Radio className="w-6 h-6 text-[#81D18A]" />
            )}
            {sidebarOpen && (
              <button
                onClick={() => setSidebarOpen(!sidebarOpen)}
                className="p-2 hover:bg-gray-100 rounded transition-colors text-gray-600"
              >
                <X className="w-5 h-5" />
              </button>
            )}
          </div>

          {!sidebarOpen && (
            <div className="px-4 pt-2 pb-4 border-b border-gray-200 flex justify-center">
              <button
                onClick={() => setSidebarOpen(!sidebarOpen)}
                className="p-2 hover:bg-gray-100 rounded transition-colors text-gray-600"
              >
                <Menu className="w-5 h-5" />
              </button>
            </div>
          )}

          {/* Navigation */}
          <nav className="flex-1 p-4">
            <ul className="space-y-2">
              {navItems.map((item) => {
                const Icon = item.icon;
                const isActive = isPathActive(item.path);

                return (
                  <li key={item.path}>
                    <Link
                      href={item.path}
                      className={`flex items-center rounded-lg transition-colors ${
                        sidebarOpen ? 'gap-3 px-4 py-3' : 'justify-center px-4 py-3'
                      } ${
                        isActive
                          ? 'bg-[#81D18A] text-white'
                          : 'text-gray-700 hover:bg-gray-100'
                      }`}
                    >
                      <Icon className="w-5 h-5 flex-shrink-0" />
                      {sidebarOpen && <span>{item.label}</span>}
                    </Link>
                  </li>
                );
              })}
            </ul>
          </nav>

          {/* Footer */}
          <div className={`p-4 border-t border-gray-200 flex ${
            sidebarOpen ? 'justify-start' : 'justify-center'
          }`}>
            <div className="flex items-center gap-3">
              <div className="w-8 h-8 bg-[#81D18A] rounded-full flex items-center justify-center flex-shrink-0 text-white">
                A
              </div>
              {sidebarOpen && (
                <div className="text-gray-900">
                  <div>관리자</div>
                </div>
              )}
            </div>
          </div>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 overflow-hidden flex flex-col">
        {children}
      </main>
    </div>
  );
}