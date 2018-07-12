'''
9:20
9:50
'''

import numpy as np
from pathlib import Path

DIM = (80, 80)

def load(flname):
    lines = Path(flname).read_text().strip().split('\n')
    mat = np.zeros(shape=DIM, dtype=int)
    for r, l in enumerate(lines):
        ls = l.split(',')
        for c, v in enumerate(ls):
            mat[r, c] = v
    return mat

def min_path_bad(mat):
    '''
    Dumb
    '''
    if min(mat.shape) == 1:
        return mat.sum()
    down = min_path(mat[1:, :])
    right = min_path(mat[:, 1:])
    return mat[0, 0] + min(down, right)

def min_path(mat):
    '''
    Dumb
    '''
    min_path_lens = np.zeros(shape=DIM, dtype=int)

    for r in reversed(range(DIM[0])):
        for c in reversed(range(DIM[1])):
            sm = mat[r, c]
            alts = []
            if r != DIM[0] - 1:
                alts.append(min_path_lens[r + 1, c])
            if c != DIM[1] - 1:
                alts.append(min_path_lens[r, c + 1])
            try:
                min_path_lens[r, c] = min(alts) + sm
            except ValueError:
                min_path_lens[r, c] = sm
    return min_path_lens[0, 0]

if __name__ == '__main__':
    mat = load('p081_matrix.txt')
    print(min_path(mat))
