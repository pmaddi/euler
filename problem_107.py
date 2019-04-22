from pathlib import Path
from numpy import array


def to_int(st):
    if st == '':
        return
    else:
        return int(st)


def prim(mat):
    in_spanning = set()
    spanning_edge_count = 0
    neighbors = []

    current = 0
    in_spanning.add(current)
    while len(in_spanning) < len(mat):
        for col, value in enumerate(mat[current]):
            if value is None:
                continue
            if col in in_spanning:
                continue
            neighbors.append((current, col, value))
            neighbors.sort(key=lambda x: x[2])
        while True:
            cur, col, value = neighbors.pop(0)
            if col not in in_spanning:
                break
        in_spanning.add(col)
        current = col
        spanning_edge_count += value
    return spanning_edge_count


if __name__ == '__main__':
    lst = [
        [
            to_int(j)
            for j
            in i.split(',')
        ]
        for i
        in Path('p107_network.txt').read_text().replace('-', '').split()
    ]
    a = array(lst)
    cnt = 0
    for r in a:
        for c in r:
            if c is None:
                continue
            cnt += c
    val = prim(a)
    print(cnt // 2 - val)
