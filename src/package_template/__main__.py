from . import __version__, __author__, __email__
from .logging_config import get_logger

logger = get_logger(__name__)

if __name__ == "__main__":
    logger.info(f"Package Template v{__version__} initialized")
    logger.info(f"Author: {__author__}")
    logger.info(f"Email: {__email__}")
