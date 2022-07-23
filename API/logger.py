import logging
import API.settings as settings
 
logging.config.fileConfig(settings.BASE_DIR / 'logging.conf', disable_existing_loggers=False)

logger = logging.getLogger(settings.ENV.values().API_TITLE)