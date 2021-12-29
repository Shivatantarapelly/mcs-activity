import unittest


# class TestPractise(unittest.TestCase):
#     def setUp(self) -> None:
#         print('set up method got executed')
#
#     def test_1(self):
#         print("test1 got executed")
#
#     def tearDown(self) -> None:
#         print("teardown method got executed")
#
#
# unittest.main()

# in the above code execution flow of methods will be setup()-->test_1-->teardown
# if there are more than one test cases

class TestPractise(unittest.TestCase):
    def setUp(self) -> None:
        print('set up method got executed')

    def test_1(self):
        print("test1 got executed")

    def test_2(self):
        print("test2 got executed")

    def tearDown(self) -> None:
        print("teardown method got executed")


# unittest.main()


# in this case the execution if methods is setup()-->test_1-->teardown than setup()-->test_2-->teardown
# using setupclass method and teardownclass method
'''
class TestPractise(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("this is setupclass method")

    def setUp(self) -> None:
        print('set up method got executed')

    def test_1(self):
        print("test1 got executed")

    def test_2(self):
        print("test2 got executed")

    def test_3(self):
        print("test3 got executed")

    def test_4(self):
        print("test4 got executed")

    def tearDown(self) -> None:
        print("teardown method got executed")

    @classmethod
    def tearDownClass(cls) -> None:
        print("this is tear down class method")


unittest.main()
'''

#  in the above case setup instance and teardown instance will execute 4 times as there are four test cases
# but setup class method and teardown class method will execute only once
