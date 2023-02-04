import logging
import re

from logging.handlers import TimedRotatingFileHandler

# Printing formatter
# formatter = logging.Formatter('%(asctime)s | %(levelname)s | [%(filename)s:%(lineno)d] | %(message)s')
formatter = logging.Formatter(
    '%(asctime)s | %(levelname)7s | [%(filename)s:%(funcName)s:%(lineno)d] — %(message)s'
)

# Stream handler for printing log to the console
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)
stream_handler.setFormatter(formatter)

# TimeRotatingHandler for saving logs in files
time_rotate_handler = TimedRotatingFileHandler(
    filename='./logs/app.log',
    when='MIDNIGHT',
    interval=1,
    backupCount=30
)
time_rotate_handler.setLevel(logging.DEBUG)
time_rotate_handler.setFormatter(formatter)
time_rotate_handler.suffix = '%Y-%m-%d.log'
time_rotate_handler.extMatch = re.compile(
    r"^\d{4}-\d{2}-\d{2}(.log)$"
)

# Add handlers to the centre logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.addHandler(stream_handler)
logger.addHandler(time_rotate_handler)