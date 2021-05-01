import pickle
from .serializer import Serializer


class PicklePacker(Serializer):
    def dump(self, obj, fp):
        with open(fp, 'wb') as file:
            pickle.dump(obj, file)

    def dumps(self, obj):
        return pickle.dumps(obj)

    def load(self, fp):
        with open(fp, 'rb') as file:
            return pickle.load(file)

    def loads(self, data):
        return pickle.loads(data)
