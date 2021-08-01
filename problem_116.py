def ways(n, tiles):
    cnt = 0
    for tile in tiles:
        cache = {}
        for sz in range(1, n + 1):
            tot = 0
            end_idx = sz - 1
            for start in range(sz):
                right_idx = start + tile - 1
                if right_idx > end_idx:
                    continue
                addtl = (
                    # cache.get(start, 0) +
                    cache.get(end_idx - right_idx, 0) +
                    1
                )
                tot += addtl
            cache[sz] = tot
        cnt += cache[n]
    return cnt

def test_ways():
    assert ways(2, [2]) == 1
    assert ways(5, [2]) == 7
    assert ways(5, [3]) == 3
    assert ways(5, [4]) == 2
    assert ways(5, [2, 3, 4]) == 12

if __name__ == "__main__":
    print(ways(50, [2, 3, 4]))
