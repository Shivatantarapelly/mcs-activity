import logging
"""
logging.basicConfig(level=logging.DEBUG, filename="..\logs\demologs.log", filemode="a",
                    format="%(asctime)s - %(levelname)s : %(message)s")
"""
# %(asctime)s for time stamp and '-' ':' is seperator can use anything and the message
# o/p will be
# 2022-02-28 14:25:04,004 - DEBUG : the addition of number is:8
# 2022-02-28 14:25:04,004 - INFO : the addition of number is:8
# 2022-02-28 14:25:04,005 - WARNING : the addition of number is:8
# 2022-02-28 14:25:04,005 - ERROR : the addition of number is:8
# 2022-02-28 14:25:04,005 - CRITICAL : the multiplication of number is:15
# ------------------   -----------        -------------------------
#    time stamp          level                  message

# if we want to change th time format we can change as below
logging.basicConfig(level=logging.DEBUG, filename="..\logs\demologs.log", filemode="a",
                    format="%(asctime)s - %(levelname)s : %(message)s", datefmt="%d/%m/%Y %I:%M:%S %p")
# then o/p will be:
# 28/02/2022 02:48:11 PM - DEBUG : the addition of number is:8
# 28/02/2022 02:48:11 PM - INFO : the addition of number is:8
# 28/02/2022 02:48:11 PM - WARNING : the addition of number is:8
# 28/02/2022 02:48:11 PM - ERROR : the addition of number is:8
# 28/02/2022 02:48:11 PM - CRITICAL : the multiplication of number is:15




class DemoLogging:
    def add_numbers(self, a, b):
        return a + b

    def mul_numbers(self, a, b):
        return a * b


dl = DemoLogging()
sum_result = dl.add_numbers(3, 5)
logging.debug("the addition of number is:{} ".format(sum_result))
logging.info("the addition of number is:{} ".format(sum_result))
logging.warning("the addition of number is:{} ".format(sum_result))
logging.error("the addition of number is:{} ".format(sum_result))
mul_result = dl.mul_numbers(3, 5)
logging.critical("the multiplication of number is:{} ".format(mul_result))
