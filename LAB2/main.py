from Packer import Packer, SerialiazeEnum


class A(object):
    def __init__(self):
        self.a = 5
        self.b = '132'
        self.sports = ['sfsdjf', 'sdsfhsdjhf']


ser = Packer.create_serializer(SerialiazeEnum.JSON)
a = A()

ser.dump(a, '/home/shprexen/PycharmProjects/Serial/file.json')
b = ser.load('/home/shprexen/PycharmProjects/Serial/file.json')
print(b)
