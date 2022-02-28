import inspect
import logging

import softest as softest


class Utils(softest.TestCase):
    def list_item_text(self, list1, value):
        for stop in list1:
            print(stop.text)
            self.soft_assert(self.assertEqual, stop.text, value)
            if stop.text == value:
                print("assert pass")
            else:
                print("aasert fail")
        self.assert_all()

# creating the custom logger

    def custom_logger(logLevel = logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        fh = logging.FileHandler("automation.log", 'w')
        formatter = logging.Formatter("%(asctime)s - %(levelname)s : %(message)s", datefmt="%d/%m/%Y %I:%M:%S %p")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger