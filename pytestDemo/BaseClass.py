import inspect
import logging

class BaseClass:
    def getLogger(self):
        # getLogger() method takes the test case name as input
        #loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(__name__)
        # FileHandler() method takes location and path of log file
        fileHandler = logging.FileHandler('logfile.log')
        # Formatter() method takes care of the log file formatting
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        # addHandler() method takes fileHandler object as parameter
        logger.addHandler(fileHandler)
        # setting the logger level
        logger.setLevel(logging.DEBUG)
        return logger
