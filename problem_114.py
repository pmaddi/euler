def ways(n):
    g = [1]
    r = [0]
    for i in range(1, n + 1):
        n_g = g[-1] + r[-1]
        g.append(n_g)
        n_r = r[-1]
        past_tack = i - 3
        if past_tack >= 0:
            n_r += g[past_tack]
        r.append(n_r)
    return g[-1] + r[-1]


def test_ways():
    assert ways(4) == 4
    assert ways(7) == 17


if __name__ == '__main__':
    print(ways(50))
