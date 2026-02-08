import inspect
import logging

class logger_class:
    @staticmethod
    def get_logger():
        log_file = logging.FileHandler(".\\Logs\\OrangeHRM.log")  # log file
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - %(lineno)d - %(message)s')
        log_file.setFormatter(formatter)
        logger = logging.getLogger(inspect.stack()[1][1]) # this takes the name of the current module
        logger.addHandler(log_file)
        logger.setLevel(logging.INFO)
        return logger