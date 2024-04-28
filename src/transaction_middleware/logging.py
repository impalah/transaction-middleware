import sys

from loguru import logger

from transaction_middleware.settings import settings

# Configurar el logger
logger.remove()
logger.add(
    sink=sys.stderr,
    level=settings.TRANSACTION_MIDDLEWARE_LOG_LEVEL,
    format=settings.TRANSACTION_MIDDLEWARE_LOG_FORMAT,
    colorize=True,
)
