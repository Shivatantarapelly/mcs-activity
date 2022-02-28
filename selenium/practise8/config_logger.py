import logging


# configuring the logger utilities

class LoggerDemo:
    def sample_logger(self):
        logger = logging.getLogger(__name__)
        # here __name__ is used when we import this logger in other module then it show the
        # module from which it is coming if we want class then we can give modulename.__name__ as parameter

        logger.setLevel(logging.DEBUG)
        # the above is to set log level
        ch = logging.StreamHandler()
        # the above will create console handler
        fh = logging.FileHandler("demologfile.log")
        # create file handler and passing the log file name
        formatter = logging.Formatter("%(asctime)s - %(levelname)s : %(message)s", datefmt="%d/%m/%Y %I:%M:%S %p")
        formatter1 = logging.Formatter("%(asctime)s - %(levelname)s : %(message)s")
        # the above is for creating formatter- how you want your logs to formatted
        ch.setFormatter(formatter)
        fh.setFormatter(formatter1)
        # adding formatter to console or file handler
        logger.addHandler(ch)
        logger.addHandler(fh)
        # adding console and file handler to logger
        logger.debug("debug log statement")
        logger.info("info log statement")
        logger.warning("warning log statement")
        logger.error("error log statement")
        logger.critical("critical log statement")


ld = LoggerDemo()
ld.sample_logger()
