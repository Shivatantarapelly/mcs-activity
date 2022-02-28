import logging

logging.basicConfig(level=logging.DEBUG, filename="..\logs\demologs.log", filemode="a")


# the above line isto setting the level so that the info an debug logs can be saved in file and
# filename where .. indicates backward to package i.e practise 8 and then logs directory location
# filemode is like append 'a', written 'w'  etc
# after executing we get logs file with filename demologs
class DemoLogging:
    def add_numbers(self, a, b):
        return a + b

    def mul_numbers(self, a, b):
        return a * b


dl = DemoLogging()
sum_result = dl.add_numbers(3, 5)
logging.debug("the addition of number is:{} ".format(sum_result))
logging.info("the addition of number is:{} ".format(sum_result))
# this debug and info will not execute in console untill we set the level
logging.warning("the addition of number is:{} ".format(sum_result))
logging.error("the addition of number is:{} ".format(sum_result))
mul_result = dl.mul_numbers(3, 5)
logging.critical("the multiplication of number is:{} ".format(mul_result))
