import datetime
import logging
import os
import sys
from logging import handlers

logger = None


def get_logger(project_name='hello-python', log_path='logs'):
    global logger
    if logger is not None:
        return logger

    logger = logging.getLogger(project_name)
    logger.setLevel(logging.INFO)

    all_log_file = os.path.join(log_path, project_name + '.log')
    all_handler = handlers.TimedRotatingFileHandler(all_log_file, when='midnight', interval=1,
                                                    backupCount=7,
                                                    atTime=datetime.time(0, 0, 0, 0))
    all_handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(message)s"))

    err_handler = logging.FileHandler(os.path.join(log_path, project_name + '-error.log'))
    err_handler.setLevel(logging.ERROR)
    err_formater = logging.Formatter("%(asctime)s %(levelname)s %(filename)s[:%(lineno)d]: %(message)s")
    err_handler.setFormatter(err_formater)

    # 输出到控制台
    std_handler = logging.StreamHandler(sys.stdout)
    std_handler.setLevel(logging.DEBUG)
    std_handler.setFormatter(err_formater)

    logger.addHandler(all_handler)
    logger.addHandler(err_handler)
    logger.addHandler(std_handler)

    return logger
