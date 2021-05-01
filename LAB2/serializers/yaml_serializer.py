import yaml
from .serializer import Serializer


class YamlPacker(Serializer):
    def dumps(self, obj):
        return yaml.dump(obj)

    def loads(self, data):
        return yaml.unsafe_load(data)
