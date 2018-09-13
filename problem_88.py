'''
Something about deciding where to draw the bars in a list of ones?

Too slow rn:
mps(113) is v slow
'''
from functools import reduce

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

def options(tpl):
    out = []
    vals = set(tpl)
    for v in vals:
        idx = tpl.index(v)
        new_tpl = tpl[:idx] + (v + 1,) + tpl[idx + 1:]
        out.append(tuple(sorted(new_tpl)))
    out = sorted(out, key=lambda x: reduce(s, x))
    return out

def mps(k):
    seen = set()
    init = tuple([1 for i in range(k)])
    queue = [init]
    while len(queue) != 0:
        tpl = queue.pop(0)
        if tpl in seen:
            continue
        else:
            seen.add(tpl)
        # print(tpl)
        if is_product_sum(tpl):
            return sum(tpl)
        opts = options(tpl)
        queue += opts

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
    # print(mps(2))
    print(sum_of(mps, 12000))
