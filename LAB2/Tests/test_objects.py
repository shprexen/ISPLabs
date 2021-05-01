class TestObjects:
    def __init__(self):
        self.num = 2
        self.string = "fdbjfskj"
        self.list = [1.2, "fshdsdf", 465, {"a": 5}]
        self.dict = {"a": 5, "b": "fdd"}


class TestClass:
    def __init__(self):
        self.string = 'a'
        self.number = 4.6


test_object = TestClass()


global_value = 5


def func():
    return global_value ** 2


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


lam_func = lambda x: x ** 5
