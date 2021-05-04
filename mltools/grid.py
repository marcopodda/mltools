from sklearn.model_selection import ParameterGrid

from .options import Options
from .serialization import load_yaml, save_yaml


class Grid:
    @classmethod
    def from_yaml(cls, path):
        hparams = load_yaml(path)
        return cls(hparams)

    def __init__(self, grid_dict):
        self._grid = ParameterGrid(grid_dict)

    def __iter__(self):
        for hparam in self._grid:
            yield Options(**hparam)

    def __getitem__(self, index):
        return Options(**self._grid[index])

    def save(self, path):
        save_yaml(self._grid.param_grid[0], path)
