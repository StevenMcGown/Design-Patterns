import logging
import logging.config
import traceback
# https://docs.python.org/3/library/logging.html#logging.basicConfig
# https://docs.python.org/3/library/logging.html#logrecord-attributes
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                    datefmt='%m/%d/%Y %H:%M:%S')

import helper

# 5 different log levels for different levels of severity (low to high)

logging.debug('This is a debug message')
logging.info('This is a info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

# Handler
logger = logging.getLogger(__name__)

stream_h = logging.StreamHandler()
file_h = logging.FileHandler('./10_Logging/logs/file.log')

#level
stream_h.setLevel(logging.WARNING) # Will only recognize Warning and above
file_h.setLevel(logging.ERROR) # Will only take in Errors and above

#format
formatter = logging.Formatter('%(name)s = %(levelname)s - %(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

#add loggers to the handler
logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is an error')
logger.critical('this is a critical error')

logging.config.fileConfig('./10_Logging/logs/logging.conf')

logger = logging.getLogger('simpleExample')
logger.debug('this is a debug message')


try:
  a = [1,2,3]
  val = a[4]
#except IndexError as e:
#  logging.error(e, exc_info=True)
except:
  logging.error('The error is %s', traceback.format_exc())
