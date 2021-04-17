class TestObjects:
    def __init__(self):
        self.num = 2
        self.string = "fdbjfskj"
        self.list = [1.2, "fshdsdf", 465, {"a": 5}]
        self.dict = {"a": 5, "b": "fdd"}


def func(a):
    print(a + 5)
    return a**2


def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
