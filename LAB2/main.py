from Packer import Packer, SerialiazeEnum


class A:
    def __init__(self):
        self.a = 5
        self.b = '132'
     #   self.sports = ['sfsdjf', 'sdsfhsdjhf']

def func(a, b):


    print(a+b)


ser = Packer.create_serializer(SerialiazeEnum.YAML)


b = A()

tu = 4

ser.dump(lambda a: a+5, '/home/shprexen/PycharmProjects/Serial/file.toml')




