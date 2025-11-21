"""
Logging configuration for package_template.

This module provides comprehensive logging setup with support for:
- Colored console output (using coloredlogs or colorlog)
- File rotation
- Configurable log levels
- Fallback to basic ANSI colors if dependencies not available
"""

import logging
import sys
from pathlib import Path
from typing import Optional


# ANSI color codes for fallback
class ANSIColors:
    """ANSI color codes for terminal output."""
    RESET = '\033[0m'
    BOLD = '\033[1m'
    
    # Foreground colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright foreground colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'


class ColoredFormatter(logging.Formatter):
    """Custom formatter with ANSI color support as fallback."""
    
    COLORS = {
        'DEBUG': ANSIColors.CYAN,
        'INFO': ANSIColors.GREEN,
        'WARNING': ANSIColors.YELLOW,
        'ERROR': ANSIColors.RED,
        'CRITICAL': ANSIColors.BOLD + ANSIColors.RED,
    }
    
    def format(self, record):
        """Format log record with colors."""
        # Save original levelname
        levelname = record.levelname
        
        # Add color to levelname
        if levelname in self.COLORS:
            record.levelname = f"{self.COLORS[levelname]}{levelname}{ANSIColors.RESET}"
        
        # Format the message
        formatted = super().format(record)
        
        # Restore original levelname
        record.levelname = levelname
        
        return formatted


def configure_project_logging(
    level: str = "INFO",
    console_colors: bool = True,
    log_file: Optional[Path] = None,
    file_level: str = "DEBUG",
) -> logging.Logger:
    """
    Configure logging for the package_template project.
    
    This function sets up logging with optional colored console output and file logging.
    It attempts to use coloredlogs or colorlog if available, falling back to basic
    ANSI colors if neither is installed.
    
    Args:
        level: Logging level for console output (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        console_colors: Whether to use colored output for console logs
        log_file: Optional path to a log file. If provided, logs will be written to this file
        file_level: Logging level for file output (if log_file is provided)
    
    Returns:
        The root logger configured with the specified settings
    
    Example:
        >>> logger = configure_project_logging(level="INFO", console_colors=True)
        >>> logger.info("This is an info message")
    """
    # Convert string levels to logging constants
    numeric_level = getattr(logging, level.upper(), logging.INFO)
    numeric_file_level = getattr(logging, file_level.upper(), logging.DEBUG)
    
    # Get root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)  # Set to DEBUG to allow all levels
    
    # Remove existing handlers to avoid duplicates
    root_logger.handlers = []
    
    # Console handler configuration
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(numeric_level)
    
    # Try to use coloredlogs first
    if console_colors:
        try:
            import coloredlogs
            
            # coloredlogs format
            field_styles = {
                'asctime': {'color': 'green'},
                'hostname': {'color': 'magenta'},
                'levelname': {'bold': True, 'color': 'black'},
                'name': {'color': 'blue'},
                'programname': {'color': 'cyan'},
            }
            
            level_styles = {
                'debug': {'color': 'cyan'},
                'info': {'color': 'green'},
                'warning': {'color': 'yellow'},
                'error': {'color': 'red'},
                'critical': {'bold': True, 'color': 'red'},
            }
            
            fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            
            coloredlogs.install(
                level=numeric_level,
                logger=root_logger,
                fmt=fmt,
                field_styles=field_styles,
                level_styles=level_styles,
            )
            
        except ImportError:
            # Try colorlog as second option
            try:
                import colorlog
                
                formatter = colorlog.ColoredFormatter(
                    '%(log_color)s%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    reset=True,
                    log_colors={
                        'DEBUG': 'cyan',
                        'INFO': 'green',
                        'WARNING': 'yellow',
                        'ERROR': 'red',
                        'CRITICAL': 'red,bg_white',
                    },
                    secondary_log_colors={},
                    style='%'
                )
                
                console_handler.setFormatter(formatter)
                root_logger.addHandler(console_handler)
                
            except ImportError:
                # Fallback to custom ANSI color formatter
                formatter = ColoredFormatter(
                    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S'
                )
                console_handler.setFormatter(formatter)
                root_logger.addHandler(console_handler)
    else:
        # No colors - plain formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        console_handler.setFormatter(formatter)
        root_logger.addHandler(console_handler)
    
    # File handler configuration (if log_file is provided)
    if log_file:
        log_file = Path(log_file)
        log_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Use RotatingFileHandler for automatic log rotation
        from logging.handlers import RotatingFileHandler
        
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=10 * 1024 * 1024,  # 10MB
            backupCount=5
        )
        file_handler.setLevel(numeric_file_level)
        
        # File logs should not have colors
        file_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(file_formatter)
        root_logger.addHandler(file_handler)
    
    return root_logger


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger with the specified name.
    
    Args:
        name: Name of the logger (typically __name__ of the calling module)
    
    Returns:
        A logger instance with the specified name
    
    Example:
        >>> logger = get_logger(__name__)
        >>> logger.info("This is an info message")
    """
    return logging.getLogger(name)
