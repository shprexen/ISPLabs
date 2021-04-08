import pickle


class PicklePacker(object):
    def dump(self, obj, fp):
        with open(fp, 'wb') as file:
            pickle.dump(obj, file)

    def dumps(self,obj):
        pickle.dumps(obj)

    def load(self, fp):
        with open(fp, 'rb') as file:
            return pickle.load(file)

    def loads(self, data):
        pickle.loads(data)
