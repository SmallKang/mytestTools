'''
日志工具类
'''
import logging
import logging.handlers as lh
import sys, os


class Logger:
    def __init__(self, logName, logFile) -> None:
        self._logger = logging.getLogger(logName)
        handler = lh.RotatingFileHandler(logFile, maxBytes=10*1024*1024, backupCount=10)
        formatter = logging.Formatter("[%(asctime)s]:[%(message)s]")
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)
        self._logger.setLevel(logging.INFO)

    def log(self, msg):
        if self._logger is not None:
            self._logger.info(msg)

    