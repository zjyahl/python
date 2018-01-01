# -*- coding: utf-8 -*-

import logging
import logging.handlers



class Logger:
    def __init__(self, logName):
        self._logger = logging.getLogger(logName)

        #logging.handlers.RotatingFileHandler('logs/myapp.log', maxBytes=100, backupCount=5)

        filehandler = logging.handlers.TimedRotatingFileHandler("myapp.log", when='D', interval=1, backupCount=0)
        filehandler.suffix = "%Y-%m-%d.log"
        filehandler.level = logging.DEBUG

        console_handler = logging.StreamHandler()
        console_handler.level = logging.DEBUG

        LOGGING_FORMAT = '[%(levelname)s %(asctime)s %(module)s: %(funcName)s %(lineno)d] %(message)s'
        DATE_FORMAT = '%y%m%d %H:%M:%S'
        formatter = logging.Formatter(LOGGING_FORMAT, DATE_FORMAT)

        filehandler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        self._logger.addHandler(filehandler)
        self._logger.addHandler(console_handler)


    @property
    def log(self):
        return self._logger

if __name__ == "__main__":
    pass