from config import log_config
import logging

class Logging:

    def __int__(self,name: str):
        """
        The constructor to initiate the object with logger name
        :param name: name of the logger
        """
        # create logger
        try:
            self.logger = logging.getLogger(name)
        except Exception as e:
            raise Exception(e)

