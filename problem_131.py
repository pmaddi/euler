"""
2    2
12   2 2 3
36   2 2 3 3
80   2 2 2 2 5
252
810
1100
1452
2366
"""

from problem_60 import prime_sieve


def is_cube(n):
    rt = int(round(n ** (1/3)))
    return rt ** 3 == n


def count(limit=10**6):
    primes = set(list(prime_sieve(limit)))
    cnt = 0
    for n_b in range(limit):
        n = n_b ** 3
        p_plus_n = (n_b + 1) ** 3
        p_cand = p_plus_n - n
        if p_cand not in primes:
            continue
        if p_cand > max(primes):
            return cnt
        nsq = (n ** 2)
        cb = nsq * p_plus_n
        result_is_cube = is_cube(cb)
        if not result_is_cube:
            continue
        cnt += 1
        print(cb, n, p_cand, nsq, p_plus_n)
    return cnt


def test_count():
    assert count(100) == 4


if __name__ == '__main__':
    # print(list(prime_sieve(10**6)))
    # print(count())
    print(count())
