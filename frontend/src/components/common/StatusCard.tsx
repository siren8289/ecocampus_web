import { ReactNode } from 'react';
import { LucideIcon } from 'lucide-react';

interface StatusCardProps {
  title: string;
  subtitle: string;
  icon: LucideIcon;
  iconBgColor: string;
  iconColor: string;
  statusIcon: ReactNode;
  statusText: string;
  statusColor: string;
  additionalInfo?: string;
  progress?: number;
}

export function StatusCard({
  title,
  subtitle,
  icon: Icon,
  iconBgColor,
  iconColor,
  statusIcon,
  statusText,
  statusColor,
  additionalInfo,
  progress,
}: StatusCardProps) {
  return (
    <div className="bg-white border border-gray-200 rounded-lg p-6">
      <div className="flex items-start justify-between mb-4">
        <div className="flex items-center gap-3">
          <div className={`p-3 ${iconBgColor} rounded-lg`}>
            <Icon className={`w-6 h-6 ${iconColor}`} />
          </div>
          <div>
            <h3 className="text-gray-900">{title}</h3>
            <p className="text-gray-600">{subtitle}</p>
          </div>
        </div>
        {statusIcon}
      </div>
      <div className={statusColor}>
        {statusText}
      </div>
      {additionalInfo && (
        <div className="mt-2 text-gray-600">
          {additionalInfo}
        </div>
      )}
      {progress !== undefined && (
        <div className="mt-2 w-full bg-gray-200 rounded-full h-2">
          <div
            className="bg-blue-600 h-2 rounded-full transition-all"
            style={{ width: `${progress}%` }}
          />
        </div>
      )}
    </div>
  );
}
