'''
def ways(n):
    cache = {}
    for num in range(1, n + 1):
        out = set([(num,)])
        for i in range(1, num//2 + 1):
            j = num - i
            j_ways = cache[j]
            for j_way in j_ways:
                out.add(tuple(sorted(j_way + (i,))))
        cache[num] = out
        print('at', num, len(cache[num]) - 1, cache[num])
    return len(cache[n]) - 1

if __name__ == '__main__':
    # assert(ways(5) == 6)
    print(ways(10))
'''
import numpy as np
def ways(n):
    tbl = np.ones((n, n + 1), dtype=int)
    for idx_i in range(1, n):
        for idx_j in range(n + 1):
            other_val_idx = idx_j - (idx_i + 1)
            if other_val_idx >= 0:
                other = tbl[idx_i, other_val_idx]
            else:
                other = 0
            tbl[idx_i, idx_j] = tbl[idx_i - 1, idx_j] + other
    return tbl[n-1, n] - 1

if __name__ == '__main__':
    assert(ways(2) == 1)
    assert(ways(5) == 6)
    print(ways(100))
