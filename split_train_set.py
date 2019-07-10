import numpy as np
import pandas as pd

def split_train_set(data, cost_validation_percentage, test_percentage, id_column, hash = hashlib.md5):
    ids = data[id_column]
    shuffled_set = np.random.permutation(len(data))

    cost_validation_set_size = int(len(data) * cost_validation_percentage)
    test_set_size = int(len(data) * test_percentage)
    train_set_size = len(data)-cost_validation_set_size-test_set_size
    
    cost_validation_set = shuffled_set[:cost_validation_set_size]
    test_set = shuffled_set[cost_validation_set_size:(test_set_size+cost_validation_set_size):1]
    train_set = shuffled_set[(test_set_size+cost_validation_set_size):]

    return data.iloc[train_set], data.iloc[cost_validation_set], data.iloc[test_set]

