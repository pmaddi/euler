'''
Bad solution.

You can just do 40 choose 20. You know there are 40 moves to make, 20 of which
must be right and 20 must be down. It is just a matter of picking which is
which.
'''
import numpy as np
def lattice_paths(size):
    size = size + 1
    grid = np.zeros((size, size), dtype=np.int)
    grid[0, :] = 1
    grid[:, 0] = 1
    for i in range(1, grid.shape[0]):
        for j in range(1, grid.shape[1]):
            grid[i, j] = grid[i - 1, j] + grid[i, j - 1]
    return grid[size - 1, size - 1]

def test_lattice_paths():
    assert(lattice_paths(0) == 1)
    assert(lattice_paths(1) == 2)
    assert(lattice_paths(2) == 6)

if __name__ == '__main__':
    test_lattice_paths()
    print(lattice_paths(20))

