import sys
import json
from pathlib import Path
from datetime import datetime
from loguru import logger

PROJECT_ROOT = Path(__file__).parent.parent.parent
LOG_DIR = PROJECT_ROOT / "logs" / datetime.now().strftime("%Y-%m-%d")
LOG_DIR.mkdir(parents=True, exist_ok=True)

logger.remove()

logger.add(
    sys.stderr,
    format="<level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
    level="INFO",
    colorize=True,
)


def json_sink(message):
    record = message.record
    log_data = {
        "timestamp": record["time"].isoformat(),
        "level": record["level"].name,
        "logger": record["name"],
        "function": record["function"],
        "line": record["line"],
        "message": record["message"],
    }
    print(json.dumps(log_data, file=sys.stderr))


log_file = LOG_DIR / "app_{time:YYYY-MM-DD}.log"
logger.add(
    str(log_file),
    format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
    level="DEBUG",
    rotation="500 MB",
    retention="30 days",
    backtrace=True,
    diagnose=True,
)

__all__ = ["logger"]
