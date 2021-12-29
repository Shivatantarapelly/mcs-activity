import unittest
from file import *
from file1 import *

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestPractise)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestPractise1)

ts = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner().run(ts)
