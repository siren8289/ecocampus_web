import { ReactNode } from 'react';
import { LucideIcon } from 'lucide-react';

interface StatCardProps {
  icon: LucideIcon;
  iconBgColor: string;
  iconColor: string;
  label: string;
  value: string | number;
  status?: ReactNode;
  className?: string;
}

export function StatCard({
  icon: Icon,
  iconBgColor,
  iconColor,
  label,
  value,
  status,
  className = '',
}: StatCardProps) {
  return (
    <div className={`bg-white rounded-lg shadow-sm border border-gray-200 p-5 ${className}`}>
      <div className="flex items-center justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className={`p-2 rounded-lg ${iconBgColor}`}>
            <Icon className={`w-5 h-5 ${iconColor}`} />
          </div>
          <div>
            <h3 className="text-gray-900">{label}</h3>
          </div>
        </div>
        {status}
      </div>
      <div className="text-gray-900">{value}</div>
    </div>
  );
}
