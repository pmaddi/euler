def f(m, n):
    g = [1]
    r = [0]
    for i in range(1, n + 1):
        n_g = g[-1] + r[-1]
        g.append(n_g)
        n_r = r[-1]
        past_tack = i - m
        if past_tack >= 0:
            n_r += g[past_tack]
        r.append(n_r)
    return g[-1] + r[-1]


def test_f():
    assert f(3, 29) == 673135
    assert f(3, 30) == 1089155
    assert f(10, 56) == 880711
    assert f(10, 57) == 1148904


def find(n, exceeds=10**6):
    def g(p):
        return f(n, p)
    lower = n
    higher = lower

    while g(higher) <= exceeds:
        lower = higher
        higher *= 2

    while True:
        mid = (lower + higher) // 2
        mid_val = g(mid)
        if mid_val < exceeds:
            lower = mid
        elif mid_val > exceeds:
            higher = mid
        else:
            return mid
        if higher - lower == 1:
            return higher


def test_find():
    assert find(10) == 57


if __name__ == '__main__':
    print(find(50))
