import unittest


class TestPractise1(unittest.TestCase):
    def setUp(self) -> None:
        print('set up method got executed')

    def test_1(self):
        print("test got executed")

    def tearDown(self) -> None:
        print("teardown method got executed")
