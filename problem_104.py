def f():
    last = 1
    cur = 1
    i = 2
    while True:
        nxt = (cur + last) % (10 ** 9)
        last = cur
        cur = nxt
        i += 1
        if set(str(cur)) == set('123456789'):
            yield i


def g():
    last = 1
    cur = 1
    i = 2
    while True:
        nxt = (cur + last)
        if nxt > (10 ** 100):
            cur = (cur - (cur % 10)) // 10
            nxt = (nxt - (nxt % 10)) // 10
        last = cur
        cur = nxt
        i += 1
        if set(str(cur)[:9]) == set('123456789'):
            yield i


def test_f():
    assert next(f()) == 541


def test_g():
    assert next(g()) == 2749


def find():
    gg = g()
    gf = f()
    n_gg = next(gg)
    n_gf = next(gf)
    while True:
        if n_gg > n_gf:
            n_gf = next(gf)
        elif n_gf > n_gg:
            n_gg = next(gg)
        else:
            return(n_gg)


if __name__ == '__main__':
    print(find())
