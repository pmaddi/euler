def primes_lt(n):
    # too slow
    nums = [0] * (n - 1)
    nums[0] = 1
    for i in range(2, int(n ** .5) + 1):
        for j in range(2, (n // i) + 1):
            if i * j < n:
                nums[i * j - 1] = 1 # is nonprime
    primes = set()
    for i in range(len(nums)):
        if not nums[i]:
            primes.add(i + 1)
    return primes


def pf(value, cache, primes):
    if value in cache:
        return cache[value]
    for p in primes:
        if value % p != 0:
            continue
        other = value // p
        opf = set(pf(other, cache, primes))
        opf.add(p)
        cache[value] = opf
        return opf


def prod(lst):
    out = 1
    for i in lst:
        out *= i
    return out


def e(k, n):
    pr = primes_lt(n + 1)
    cache = {i: {i} for i in pr}
    cache[1] = {1}
    pr_lst = sorted(list(pr))
    for v in range(1, n + 1):
        pf(v, cache, pr_lst)
    rads = [(prod(v), k) for k, v in cache.items()]
    rads.sort()
    return rads[k - 1][1]


def test_e():
    assert e(4, 10) == 8
    assert e(6, 10) == 9


if __name__ == '__main__':
    # e(4, 10)
    # print(primes_lt(10000))
    print(e(10000, 100000))
