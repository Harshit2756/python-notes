from functools import wraps

# this decorator
def my_decorator_a(func):
    # this is used to preserve the original function's metadata like its name and docstring etc.
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

# Using the decorator
@my_decorator_a
def greet():
    print("Hello from decorators class from chaicode")


greet()
print(greet.__name__)