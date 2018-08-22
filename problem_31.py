'''
1p, 2p, 5p, 10p, 20p, 50p, E1 (100p) and E2 (200p)

'''

COINS = [1, 2, 5, 10, 20, 50, 100, 200]


def ways(p):
    cts = [0 for i in range(p + 1)]

    cts[0] = 1
    for i in range(len(COINS)):
        for j in range(COINS[i], p + 1):
            # cts[j] is the ways to make j without COINS[i] or above
            cts[j] += cts[j - COINS[i]]
    return cts[p]

def dways(COINS, p):
    cts = [0 for i in range(p + 1)]

    cts[0] = 1
    for i in range(len(COINS)):
        for j in range(COINS[i], p + 1):
            # cts[j] is the ways to make j without COINS[i] or above
            cts[j] += cts[j - COINS[i]]
    return cts[p]


if __name__ == '__main__':
    print(ways(1))
    assert(ways(0) == 1)
    assert(ways(1) == 1)
    assert(ways(2) == 2)
    assert(ways(3) == 2)
    assert(ways(4) == 3)
    print(ways(5))
    assert(ways(5) == 4)
    print(ways(200))
