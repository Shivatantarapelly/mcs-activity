import pytest


@pytest.fixture()
def setUp():
    print("open browser")
    print("login")
    print("browse product")
    yield
    print("logoff")
    print("close browser")
    # here before yield code will execute before every function and at last the remaining code will get execute
    # to execute like that we have inherit this method to another where we want to use


def test_additem(setUp):
    print("Item added successfully")


def test_remitem(setUp):
    print("Item removed successfully")
