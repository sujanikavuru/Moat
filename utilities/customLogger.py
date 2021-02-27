import logging


class LogGeneration:
    @staticmethod
    def loggen():

        logging.basicConfig(filename="../Logs/automation.log", format='%(asctime)s: %(levelname)s: %(message)s',
                            datefmt='%m%d%Y %I:%M:%S %P', filemode='a')
        log = logging.getLogger()
        log.setLevel(logging.INFO)
        return log
