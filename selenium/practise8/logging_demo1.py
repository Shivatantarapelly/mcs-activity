# DEBUG - Detailed information typically of interest only when diagnosing problem
# INFO - confirmation that things are working as expected
# WARNING - An indication that something unexpected happened or indicative of some problem in the near future.
# (eg.disk space low). the software is still working as expected
# ERROR - Due to more serious problems the software has not been able to perform some function
# CRITICAL - A serious error, indicating that the program itself may be unable to continue running
import logging


class DemoLogging:
    def add_numbers(self, a, b):
        return a + b

    def mul_numbers(self, a, b):
        return a * b


dl = DemoLogging()
sum_result = dl.add_numbers(3, 5)
logging.warning("the addition of number is:{} ".format(sum_result))
logging.error("the addition of number is:{} ".format(sum_result))
mul_result = dl.mul_numbers(3, 5)
logging.critical("the multiplication of number is:{} ".format(mul_result))
