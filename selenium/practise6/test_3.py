# this to see how the conf_test file works
# in fixture to execute the setup and teardown script we use to write the fixture here it self like below
import pytest

"""
@pytest.fixture()
def setUp():
    print("open browser")
    print("login")
    print("browse product")
    yield
    print("logoff")
    print("close browser")
"""

# but we can write this function in conf.py file and can execute in same way
"""
def test_additem(tc_setup):
    print("Item added successfully")


def test_remitem(tc_setup):
    print("Item removed successfully")
"""


# even if we remove tc_setup we can execute as same like above as we have given autouse = True in conftest.py file
def test_additem():
    print("Item added successfully")


def test_remitem():
    print("Item removed successfully")
