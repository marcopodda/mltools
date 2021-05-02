import socket
from datetime import datetime
from argparse import Namespace
from pathlib import Path


def default_exp_name() -> str:
    hostname = socket.gethostname()
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    return f"{date}@{hostname}"


class ExperimentBase:
    @classmethod
    def load(cls, root, name):
        return cls(root, name, exist_ok=True)

    def __init__(self, root, name=None, exist_ok=False) -> None:
        self.name = name or default_exp_name()
        self.build_folder_structure(root, exist_ok)

    def build_folder_structure(self, root, exist_ok) -> None:
        self.dirs = Namespace()
        self.dirs.root = Path(root) / self.name
        self.dirs.root.mkdir(parents=True, exist_ok=exist_ok)

        self.dirs.logs = self.dirs.root / "logs"
        self.dirs.logs.mkdir(exist_ok=exist_ok)

        self.dirs.ckpt = self.dirs.root / "ckpt"
        self.dirs.ckpt.mkdir(exist_ok=exist_ok)
