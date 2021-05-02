import numpy as np


def split(outer_splitter, inner_splitter, X, y, groups=None):
    indices = np.arange(len(X))

    splits = []
    for dev_idx, test_idx in outer_splitter.split(indices, y, groups=groups):
        test_indices = indices[test_idx]
        dev_indices = indices[dev_idx]
        dev_targets = y[dev_idx]
        dev_groups = groups[dev_idx] if groups else None

        dev_splits = []
        for tr_idx, val_idx in inner_splitter.split(dev_indices, dev_targets, groups=dev_groups):
            train_idxs = dev_indices[tr_idx]
            valid_idxs = dev_indices[val_idx]
            dev_splits.append({"train": train_idxs, "valid": valid_idxs})
        splits.append({"test": test_indices, "dev": dev_splits})

    return splits
