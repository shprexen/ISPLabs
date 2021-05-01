import toml
from .serializer import Serializer


class TomlPacker(Serializer):
    def dumps(self, obj):
        return toml.dumps(super().dumps(obj))

    def loads(self, string):
        return super().loads(toml.loads(string))
