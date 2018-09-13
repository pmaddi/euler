'''
Something about deciding where to draw the bars in a list of ones?

Too slow rn:
    Starts to get pretty slow around 1800
'''
from functools import reduce

WAY_CACHE = {}

def p(x, y):
    return x * y

def s(x, y):
    return x + y

def sums(lst):
    return reduce(p, lst), reduce(s, lst)

def is_product_sum(lst):
    l, r = sums(lst)
    return l == r

def test_is_product_sum():
    assert(is_product_sum((2, 2)))
    assert(is_product_sum((1, 2, 3)))
    assert(not is_product_sum((1, 2, 4)))

def ways_to_make(n):
    if n in WAY_CACHE:
        return WAY_CACHE[n]
    if n in [1, 2]:
        return [(n,)]
    out = []
    for i in range(2, int(n ** .5) + 1):
        d = n // i
        if not d * i == n:
            continue
        # d divides n
        ws = ways_to_make(d)
        for w in ws:
            out.append(tuple(sorted(w + (i,))))
    ret = sorted(set([(n,)] + out))
    WAY_CACHE[n] = ret
    return ret

def test_ways_to_make():
    assert(ways_to_make(1) == [(1,)])
    assert(ways_to_make(2) == [(2,)])
    assert(ways_to_make(3) == [(3,)])
    assert(ways_to_make(4) == [(2,2), (4,)])
    assert(ways_to_make(6) == [(2,3), (6,)])
    assert(ways_to_make(8) == [(2,2,2), (2, 4), (8,)])

def mps(k):
    orig_k = k
    while True:
        ways = ways_to_make(k)
        for way in ways:
            if len(way) > orig_k:
                continue
            lst = tuple([1 for i in range(orig_k - len(way))])
            nlst = lst + way
            assert(len(nlst) == orig_k)
            if is_product_sum(nlst):
                return k
        k += 1

def sum_of(fn, max_k):
    st = set()
    for i in range(2, max_k + 1):
        print(i)
        st.add(fn(i))
    return sum(st)

def test_mps():
    assert(mps(2) == 4)
    assert(mps(3) == 6)
    assert(mps(4) == 8)
    assert(mps(5) == 8)
    assert(mps(6) == 12)

def test_sum_of():
    assert(sum_of(mps, 6) == 30)
    assert(sum_of(mps, 12) == 61)

if __name__ == '__main__':
    print(mps(3421))
    # print(sum_of(mps, 12000))
