__author__ = 'naveen'

import os
import logging
import logging.handlers
import time
import glob


def app_logger(name, filename='crawler.log'):
    """
    Generic logger implementation
    usage : main module : logger = log.app_logger('gmsat')
            Sub module : logger = logging.getLogger('gmsat')

    :param name:
    :param filename:
    :return:
    """
    logger_level = '20'
    logger_format = '[%(asctime)s] [%(levelname)s] [%(module)s.%(funcName)s (%(lineno)d)] %(message)s'

    log_file_path = glob.glob(filename)[0]
    # log_file_path = os.path.join(log_conf['log_path'], 'crawler_%s.log' % crawler_started_at_str)
    log_level = {'0': logging.NOTSET, '10': logging.DEBUG, '20': logging.INFO, '30': logging.WARNING,
                 '40': logging.ERROR, '50': logging.CRITICAL, }

    # Check if log exists and should therefore be rolled
    needRoll = os.path.isfile(log_file_path)

    # handler = logging.FileHandler(filename=log_file_path)
    # Add the log message handler to the logger
    handler = logging.handlers.RotatingFileHandler(filename=log_file_path, backupCount=15)

    formatter = logging.Formatter(fmt=logger_format)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(log_level.get(logger_level, logging.INFO))
    logger.addHandler(handler)
    # This is a stale log, so roll it
    if needRoll:
        # Add timestamp
        logger.info('\n---------\nLog closed on %s.\n---------\n' % time.asctime())

        # Roll over on application start
        logger.handlers[0].doRollover()

    # Add timestamp
    logger.info('\n---------\nLog started on %s.\n---------\n' % time.asctime())

    print 'Log Level : {0} Log Path : {1}'.format(logger_level, log_file_path)
    return logger
