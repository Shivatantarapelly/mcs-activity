# this conftest.py file is used for writing the script which will execute script which we want to
# execute for every function or class or which we need execute every time like setup and teardown method
# using fixture etc

# here file name should be conftest.py and method name should be tc_setup
import pytest

"""
@pytest.fixture()
def tc_setup():
    print("open browser")
    print("login")
    print("browse product")
    yield
    print("logoff")
    print("close browser")
"""

# we can use autouse = True to execute the fixture for every method with out inheriting function
"""
@pytest.fixture(autouse=True)
def tc_setup():
    print("open browser")
    print("login")
    print("browse product")
    yield
    print("logoff")
    print("close browser")
"""

# we can also use scope parameter in fixture to use the fixture for class, function, package, session, module etc
# we want to use this fixture
"""
@pytest.fixture(scope="package", autouse=True)
def tc_setup():
    print("open browser")
    print("login")
    print("browse product")
    yield
    print("logoff")
    print("close browser")
"""


# function : will execute for every method in file
# class : will execute for every class in file
# module : will execute for every file
# session: will execute for every session
# package: will execute for every package


# we can use parameterization in this file for adding option like open browser according to we type in command line
# ex:
@pytest.fixture(scope="package", autouse=True)
def tc_setup(browser):
    if browser == "chrome":
        print("launch chrome")
    elif browser == "edge":
        print("launch edge")
    else:
        print("enter valid browser")
    # here instead of browser we can give browser config's according to which we type in cmd like if we type chrome
    # then chrome browser will open like that
    print("login")
    print("browse product")
    yield
    print("logoff")
    print("close browser")


# but in order to add option we use default method

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")
