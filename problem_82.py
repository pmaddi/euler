'''
for column in columns
    for i in column
        for j in column
            z = i thru j + memoized[j]
        next memoized [i] = min z
'''

import numpy as np
from problem_81 import load

if __name__ == '__main__':
    mat = load('p082_matrix.txt')
    print(mat)
