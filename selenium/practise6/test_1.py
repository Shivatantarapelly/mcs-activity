import pytest


@pytest.mark.shiva
def test_login():
    print("login successful")


def test_logoff():
    print("logged out")


def test_calculation():
    assert 2 + 2 == 4


# file name can be start with or end with test where as method should start with test and to execute enter pytest
# in terminal then all the test method with all test files will execute
# to execute particular file use pytest filename.py in terminal
# pytest -v  where v is verbose will give o/p with fuctions with status like passed or failed
# pytest -q gives just how many test case passed and sec for executing
# pytest -h for help to get all commands
# pytest -v -s , -v will give all the details filename, method name, status and s will give print statements
# pytest -vsk keyword, will give same as above but only method name have k keyword

