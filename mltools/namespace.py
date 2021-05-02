from argparse import Namespace
from .serialization import load_yaml, save_yaml


class NamespaceDict(Namespace):
    @classmethod
    def from_dict(cls, attrdict):
        return cls(**attrdict)

    @classmethod
    def from_yaml(cls, path):
        attrdict = load_yaml(path)
        return cls.from_dict(attrdict)

    def to_dict(self):
        return vars(self)

    def save(self, path):
        attrdict = self.to_dict()
        save_yaml(attrdict, path)

    def __getitem__(self, name):
        attrdict = self.to_dict()
        return attrdict[name]

    def __contains__(self, key):
        attrdict = self.to_dict()
        return key in attrdict