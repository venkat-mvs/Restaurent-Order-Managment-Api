import logging
import settings

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

logger = logging.getLogger(settings.ENV.values().API_TITLE)