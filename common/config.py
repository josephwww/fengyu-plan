import logging
import datetime

current_utc_time = datetime.datetime.utcnow().strftime('%Y%m%d%H%M%S')
LOG_FILE = "log/{time}.log".format(time=current_utc_time)
LOG_LEVEL = logging.DEBUG
