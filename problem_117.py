def ways(n, tiles):
    cnts = [0] * (max(tiles) * n + 1)
    cnts[0] = 1
    for i in range(0, n):
        for tile in tiles:
            cnts[i + tile] += cnts[i]
    return cnts[n]

def test_ways():
    assert ways(5, [1, 2, 3, 4]) == 15

if __name__ == "__main__":
    print(ways(50, [1, 2, 3, 4]))
