# it allows us to define mutliple sets of arguments and those arguments are taken iteratively to execute
# for ex: in testing scenario we have login page where we need to test with different parameters like
# both valid data, bothe invalid data, onvalid and other invalid like cases
# parameterization is available at several steps
# pytest.fixture() allows one to parametrize the fixture function
# @pytest.mark.parameterize allows one to define multiple sets of arguments and the fixtures at test function or class
# pytest _generate_test allows one to define custom parametrization schemes or extensions


# using pytest.fixtures to parametrize
# we have to use same parameters like params, request, param which is default
import pytest

"""
@pytest.fixture(params=["a", "b"])
def demo_fixture(request):
    print(request.param)


def test_login(demo_fixture):
    print("login successful")
    
# in above the method test_login execute two times i.e once with a and next with b
"""


# now using marker


@pytest.mark.parametrize("a, b, res", [(4, 9, 13), (5, 5, 11), (12, 12, 24)])
def test_add(a, b, res):
    assert a + b == res

# in the above method the tuples are iterated and the test case will execute 3times and give result of three values
