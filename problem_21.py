import numpy as np

def make_divisor_sum(n):
    divisor_sum = np.zeros(n, dtype=int)
    for i in range(1, n + 1):
        for j in range(2, n // i + 1):
            if i * j <= n:
                v = divisor_sum[(i * j) - 1]
                divisor_sum[(i * j) - 1] = v + i
    return divisor_sum

def test_make_divisor_sum():
    d = make_divisor_sum(10)
    assert(d[10 - 1] == (1 + 2 + 5))
    d = make_divisor_sum(1000)
    assert(d[220 - 1] == 284)
    assert(d[284 - 1] == 220)

def amiciable_sum_under(n):
    divisor_sum = make_divisor_sum(n)
    out = 0
    for i in range(1, n + 1):
        ds = divisor_sum[i - 1]
        if ds <= n:
            if i != ds and i == divisor_sum[ds - 1]:
                out += ds
    return out

if __name__ == '__main__':
    test_make_divisor_sum()
    print(amiciable_sum_under(10000))
