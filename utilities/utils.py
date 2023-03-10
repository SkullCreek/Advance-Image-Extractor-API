from config import log_config
import logging


class CustomLogging:

    def __init__(self, name: str):
        """
        The constructor to initiate the object with logger name
        :param name: name of the logger
        """
        # create logger
        try:
            self.logger = logging.getLogger(name)
        except Exception as e:
            raise Exception(e)

    def initialize_logger(self, path):
        """
        Initializes the logger by setting level, creating formatter and file handler
        """
        try:
            if len(self.logger.handlers) == 0:
                # Setting the level
                logging_level = log_config.log_level
                if logging_level == "ERROR":
                    self.logger.setLevel(logging.ERROR)
                elif logging_level == "DEBUG":
                    self.logger.setLevel(logging.DEBUG)

                # Creating formatter
                formatter = logging.Formatter('%(levelname)s - %(asctime)s : %(name)s - %(message)s.')

                # Creating file handlers
                file_handler = logging.FileHandler(path)

                # Adding formatter to file handler
                file_handler.setFormatter(formatter)

                # Adding file handler to logger
                self.logger.addHandler(file_handler)

        except Exception as e:
            raise Exception(e)

    def append_message(self, logging_statement, logging_level):
        """
        Append logging message to the logging file
        :param logging_statement: The message which will get logged
        :param logging_level: logging level can be info, warning, error or exception
        """
        try:
            if logging_level == "info":
                self.logger.info(logging_statement)
            elif logging_level == "warning":
                self.logger.warning(logging_statement)
            elif logging_level == "error":
                self.logger.error(logging_statement)
            elif logging_level == "exception":
                self.logger.exception(logging_statement)
        except Exception as e:
            raise Exception(e)
