# customized middlewares using function
'''
def my_middleware(get_response):
    print("one time initialization")

    def my_functon(request):
        print("this is before view")
        response = get_response(request)  # here it will execute the code in views
        print("this is after view")
        return response

    return my_functon
'''

# customized middlewares using class

"""
class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("one time initialization")

    def __call__(self, request):
        print("this is before view")
        response = self.get_response(request)
        print("this is after the view")
        return response
"""


# using more than one customized middleware

"""
class PythonMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("one time python initialization")

    def __call__(self, request):
        print("this is before python view")
        response = self.get_response(request)
        print("this is after the python view")
        return response


class JavaMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("one time Java initialization")

    def __call__(self, request):
        print("this is before Java view")
        response = self.get_response(request)
        print("this is after the Java view")
        return response


class CMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("one time C initialization")

    def __call__(self, request):
        print("this is before C view")
        response = self.get_response(request)
        print("this is after the C view")
        return response
"""