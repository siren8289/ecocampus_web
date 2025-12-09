import { ButtonHTMLAttributes, ReactNode } from 'react';

interface IconButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  icon: ReactNode;
  variant?: 'primary' | 'secondary' | 'danger' | 'ghost';
  size?: 'sm' | 'md' | 'lg';
  tooltip?: string;
}

export function IconButton({
  icon,
  variant = 'ghost',
  size = 'md',
  tooltip,
  className = '',
  ...props
}: IconButtonProps) {
  const variants = {
    primary: 'text-blue-600 hover:bg-blue-50',
    secondary: 'text-gray-600 hover:bg-gray-100',
    danger: 'text-red-600 hover:bg-red-50',
    ghost: 'text-gray-600 hover:bg-gray-100',
  };

  const sizes = {
    sm: 'p-1',
    md: 'p-2',
    lg: 'p-3',
  };

  return (
    <button
      className={`rounded transition-colors ${variants[variant]} ${sizes[size]} ${className}`}
      title={tooltip}
      {...props}
    >
      {icon}
    </button>
  );
}
