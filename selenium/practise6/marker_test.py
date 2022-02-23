import pytest


# in pytest there is markers concept where we can do custom marking and also we have built in markers
# these markers are used as decorators on function which helps to execute certain set of function which
# having decorator with a same expression
# we can use pytest -m expresion  where expression is in decorator like ex: @pytest.mark.sanity
# so we use pytest -m sanity
# pytest --markers will give all builtin markers like skip and xfail
# we use like @pytest.mark.skip will skip the execuion of this method when you use pytest to execute
# we use like @pytest.mark.xfail will not execute but not show error as test failed. if the fuctionality of
# ay function is not completed at that point we use this xfail

@pytest.mark.shiva
def test_sum():
    assert 4 + 5 == 9


@pytest.mark.skip
# here it will skip the testing the method and give as skipped
def test_skip():
    print("to test the skip marker")


@pytest.mark.xfail
# here if the test fail it gives xfail and test passed then it gives xpass but no error that test case failed
def test_diff():
    assert 4 + 5 == 9


