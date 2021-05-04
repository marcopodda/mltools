from argparse import Namespace
from .serialization import load_yaml, save_yaml


class Options(Namespace):
    @classmethod
    def from_dict(cls, attrdict):
        return cls(**attrdict)

    @classmethod
    def from_yaml(cls, path):
        attrdict = load_yaml(path)
        return cls.from_dict(attrdict)

    def to_yaml(self, path):
        attrdict = self.to_dict()
        save_yaml(attrdict, path)
    
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
    
    def update(self, *args, **kwargs):
        for i, obj in enumerate(args, 1):
            if isinstance(obj, Namespace):
                obj = vars(obj)
            elif isinstance(obj, Mapping):
                obj = dict(obj)
            else:
                raise TypeError(f"Unsupported type for positional argument #{i}: {type(obj)}")

            for name, value in obj.items():
                if name != "self":
                    self.__dict__[name] = value

        for name, value in kwargs.items():
            self.__dict__[name] = value
