from argparse import Namespace
from collections import Mapping

from .namespace import NamespaceDict


class Config(NamespaceDict):
    @classmethod
    def from_namespace(cls, namespace):
        cfg = vars(namespace)
        return cls(**cfg)
