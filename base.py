import logging 

formatter = logging.Formatter(
    "%(levelname)s:%(asctime)s:%(module)s: %(message)s"
)
sh = logging.StreamHandler()
sh.setFormatter(formatter)
logger = logging.getLogger(__name__)
logger.addHandler(sh)
logger.setLevel(logging.DEBUG)

class BaseDrinkClass(object):
    def __init__(self) -> None:
        super().__init__()
        self.logger = logger

    def set_level(self, log_level):
        return self.logger.setLevel(log_level)

    def get_level(self):
        return self.logger.level

    def debug(self, message: str):
        return self.logger.debug(message)

    def info(self, message: str):
        return self.logger.info(message)

    def error(self, message: str):
        return self.logger.error(message)

    def warn(self, message: str):
        return self.logger.warning(message)

    def critical(self, message: str):
        return self.logger.critical(message)

    def exception(self, message: str):
        return self.logger.exception(message)
