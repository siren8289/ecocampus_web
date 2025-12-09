import { ReactNode } from 'react';
import { AlertCircle, Info, CheckCircle, AlertTriangle } from 'lucide-react';

interface InfoBoxProps {
  title?: string;
  children: ReactNode;
  variant?: 'info' | 'success' | 'warning' | 'danger';
  className?: string;
}

export function InfoBox({ title, children, variant = 'info', className = '' }: InfoBoxProps) {
  const variants = {
    info: {
      bg: 'bg-blue-50',
      border: 'border-blue-200',
      icon: <Info className="w-5 h-5 text-blue-600" />,
      titleColor: 'text-blue-900',
    },
    success: {
      bg: 'bg-green-50',
      border: 'border-green-200',
      icon: <CheckCircle className="w-5 h-5 text-green-600" />,
      titleColor: 'text-green-900',
    },
    warning: {
      bg: 'bg-orange-50',
      border: 'border-orange-200',
      icon: <AlertTriangle className="w-5 h-5 text-orange-600" />,
      titleColor: 'text-orange-900',
    },
    danger: {
      bg: 'bg-red-50',
      border: 'border-red-200',
      icon: <AlertCircle className="w-5 h-5 text-red-600" />,
      titleColor: 'text-red-900',
    },
  };

  const config = variants[variant];

  return (
    <div className={`p-4 ${config.bg} border ${config.border} rounded-lg ${className}`}>
      {title && (
        <div className="flex items-center gap-2 mb-2">
          {config.icon}
          <h4 className={config.titleColor}>{title}</h4>
        </div>
      )}
      <div className="text-gray-600">{children}</div>
    </div>
  );
}
