'''
for column in columns
    for i in column
        for j in column
            z = i thru j + memoized[j]
        next memoized [i] = min z
'''

import numpy as np
from problem_81 import load


def min_paths_bewteen(a, b):
    """
    :param a: numpy array col
    :param b: numpy array col
    :returns: a numpy array col that has the lowest cost way from a[i] to
    anywhere in b for all i
    """
    l = len(a)
    assert(l == len(b))
    out = np.zeros(shape=(l,), dtype=int)
    for st in range(l):
        vals = []
        for end in range(l):
            left_idx = min(st, end)
            right_idx = max(st, end)
            vals.append(a[left_idx: (right_idx + 1)].sum() + b[end])
        out[st] = min(vals)
    return out

def test_min_paths_between():
    a = np.array([1,2,1])
    b = np.array([10,20,1])
    out = np.array([5, 4, 2])
    assert((min_paths_bewteen(a, b) == out).all())
    a = np.array([1,2,1])
    b = np.array([0,0,0])
    out = np.array([1, 2, 1])
    assert((min_paths_bewteen(a, b) == out).all())

def min_right_down_up_path(arr):
    """
    :param arr: array
    :returns: the min path going from the left side to the right
    """
    zero = np.zeros(shape=(arr.shape[0],), dtype=int)
    lcol_idx = arr.shape[1] - 1
    rcol = zero
    lcol = arr[:, lcol_idx]
    while True:
        rcol = min_paths_bewteen(lcol, rcol)

        lcol_idx -= 1
        lcol = arr[:, lcol_idx]

        if lcol_idx < 0:
            break
    return min(rcol)



def test_min_right_down_up_path():
    a = np.array(
        [[1,2,1],
         [10,20,1]]).T
    assert(min_right_down_up_path(a) == 2)
    a = np.array(
        [
         [1,20,50],
         [1,2,1],
         [10,20,1]]).T
    assert(min_right_down_up_path(a) == 6)





if __name__ == '__main__':
    test_min_paths_between()
    test_min_right_down_up_path()
    mat = load('p082_matrix.txt')
    print(min_right_down_up_path(mat))
    # print(mat)
