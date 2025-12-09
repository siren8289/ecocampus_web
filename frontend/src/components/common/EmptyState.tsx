import { ReactNode } from 'react';

interface EmptyStateProps {
  message: string;
  icon?: ReactNode;
  className?: string;
}

export function EmptyState({ message, icon, className = '' }: EmptyStateProps) {
  return (
    <div className={`text-center py-8 text-gray-500 ${className}`}>
      {icon && <div className="mb-4 flex justify-center">{icon}</div>}
      {message}
    </div>
  );
}
