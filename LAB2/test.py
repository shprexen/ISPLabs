from main import SerialiazeEnum
import pickle
import inspect
import dis
class Class(object):
    def __init__(self):
        self.a = 'dfsdfsd'

    def xui(self):
        pass


def func(b: 1, c: 3, a: 5):
    a = 7
    print(a)
    return a


def fun_to_YAML(fun):
    func_name = func.__code__.co_name
    func_args = func.__code__.co_varnames
    str = 'FunctionName: ' + func_name
    str = str + '\nArguments:'
    for i in range(len(func_args)):
        str += '\n- ' + func_args[i]
    return str


def fun_to_json(fun):
    func__code = inspect.getsourcelines(fun)
    func_name = func.__code__.co_name
    func_args = func.__code__.co_varnames
    str = '{"FunctionName:"' + ' "{}"'.format(func_name)
    str += ', "Arguments": ['
    for i in range(len(func_args)):
        if i != (len(func_args) - 1):
            str += '{}, '.format(func_args[i])
        else:
            str += '{}'.format(func_args[i])
    str += ', "Function code: ' + func__code
    str += ']}'

    return str


def fun_to_pickle(func, fp):
    with open('fp', 'wb') as file:
        pickle.dump(func, file)

def func_to_yaml(func):
    func_name = func.__code__.co_name
    func_args = func.__code__.co_varnames
    str = 'FunctionName: ' + func_name
    str = str + '\nArguments:'
    for i in range(len(func_args)):
        str += '\n- ' + func_args[i]
    return str


def serialize_func(func, type):
    if type is SerialiazeEnum.JSON:
        return fun_to_json(func)
    if type is SerialiazeEnum.YAML:
        return fun_to_YAML(func)
    if type is SerialiazeEnum.TOML:
        return fun_to_json(func)
    if type is SerialiazeEnum.PICKLE:
        return fun_to_json(func)

print(serialize_func(func, SerialiazeEnum.JSON))

