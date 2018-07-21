import numpy as np
from problem_81 import load
import unittest


def whichmin(dt, avoid):
    msf = None
    out = None
    for k, v in dt.items():
        if k in avoid:
            continue
        if msf is None or v < msf  :
            out = k
            msf = v
    return out


def neighboars(i, j):
    return [
            (i, j - 1),
            (i, j + 1),
            (i + 1, j),
            (i - 1, j),
            ]

def min_path_to_from(arr, start_node, target_node):
    nodes = set()
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            nodes.add((i, j))

    explored = set()
    distances = {start_node: arr[start_node]}

    exploring = start_node
    while target_node not in explored:
        ns = neighboars(*exploring)
        for n in ns:
            if n in nodes:# and n not in explored:
                weight = arr[n]
                new_dist = weight + distances[exploring]
                distances[n] = min(new_dist, distances.get(n, 1e10))
        explored.add(exploring)
        exploring = whichmin(distances, explored)
    ar = np.zeros(shape=arr.shape)
    for k, v in distances.items():
        ar[k] = v
    return distances[target_node]

def min_path(arr):
    start_node = (0, 0)
    target_node = (arr.shape[0] - 1, arr.shape[1] - 1)
    return min_path_to_from(arr, start_node, target_node)

class Test83(unittest.TestCase):
    def test_min_path(self):
        arr = np.array([[131]]).T
        self.assertEqual(min_path(arr), 131)
        arr = np.array([[131, 1], [121, 2]]).T
        self.assertEqual(min_path(arr), 134)
        arr = np.array([
            [131, 201],
            [673, 96 ]])
        self.assertEqual(min_path(arr), 428)
        arr = np.array([
            [131, 201, 630, 537, 805],
            [673, 96, 803, 699, 732],
            [234, 342, 746, 497, 524],
            [103, 965, 422, 121, 37],
            [18, 150, 111, 956, 331]]).T
        self.assertEqual(min_path(arr), 2297)

    def test_main_path_to_from(self):
        arr = np.array([
            [131, 201,],
            [673, 96, ],
            [234, 342,],
            [103, 965,],
            [18, 150, ]]).T
        self.assertEqual(min_path_to_from(arr, (0, 0), (1, 0)), 332)
        self.assertEqual(min_path_to_from(arr, (0, 0), (1, 1)), 428)
        self.assertEqual(min_path_to_from(arr, (0, 0), (1, 2)), 770)
        self.assertEqual(min_path_to_from(arr, (0, 0), (0, 2)), 1004)

if __name__ == '__main__':
    # unittest.main()
    mat = load('p083_matrix.txt')
    print(min_path(mat))
