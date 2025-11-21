from .logging_config import configure_project_logging, get_logger
from importlib.metadata import metadata as pkg_metadata, PackageNotFoundError


logger = configure_project_logging(level="INFO", console_colors=True)
try:
    _md = pkg_metadata("{{PROJECT_NAME}}")
    __version__ = _md["Version"] if "Version" in _md else "0.0.0"
    __author__ = _md["Author"] if "Author" in _md else ""
    __email__ = _md["Author-email"] if "Author-email" in _md else ""
except PackageNotFoundError:
    __version__ = "0.0.0"
    __author__ = ""
    __email__ = ""

__all__ = [
    "configure_project_logging",
    "get_logger",
    "logger",
]
