from argparse import Namespace
from collections import Mapping

from .namespace import NamespaceDict


class Config(NamespaceDict):
    @classmethod
    def from_namespace(cls, namespace):
        cfg = vars(namespace)
        return cls(**cfg)

    def update(self, *args, **kwargs):
        for i, obj in enumerate(args, 1):
            if isinstance(obj, Namespace):
                obj = vars(obj)
            elif isinstance(obj, Mapping):
                obj = dict(obj)
            else:
                raise TypeError(f"Unsupported type for positional argument #{i}: {type(obj)}")

            for name, value in obj.items():
                self.__dict__[name] = value

        for name, value in kwargs.items():
            self.__dict__[name] = value