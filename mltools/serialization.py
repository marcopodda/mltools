import yaml
import json
from pathlib import Path


def load_yaml(path_or_str):
    path = Path(path_or_str)
    return yaml.load(path.open("r"), Loader=yaml.SafeLoader)


def save_yaml(obj, path_or_str):
    path = Path(path_or_str)
    return yaml.dump(obj, path.open("w"))


def load_json(path_or_str):
    path = Path(path_or_str)
    return json.load(path.open("r"))


def save_json(obj, path_or_str):
    path = Path(path_or_str)
    return json.dump(obj, path.open("w"))