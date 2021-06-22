import logging

class LogGeneration:

    @staticmethod
    def loggen():
        logging.basicConfig(filename="./Configurations/Logs/automation.log",
                            format='(asctime)s: %(levelname)s:%(message)s', datefmt='%m/%d/%y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

