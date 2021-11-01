import logging
from logging.handlers import RotatingFileHandler
#Rotating file handlers
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2KB, and keep backup logs app.log.1, app.log.2 , etc.
handler = RotatingFileHandler('10_Logging/logs/app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10000):
    logger.info('Hello, world!')
