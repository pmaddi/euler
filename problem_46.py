import numpy as np
import math

def primes_lt(n):
    '''too slow'''
    nums = np.zeros(n - 1)
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

def double_squares_lt(n):
    vl = math.ceil(int((n / 2) ** .5))
    for i in range(1, vl + 1):
        yield 2 * (i**2)

def mark_under(n):
    pr = primes_lt(n)
    dbl_sqr = list(double_squares_lt(n))

    composite_odd = (
            i for i in range(2, n)
            if i not in pr and i % 2 == 1)

    found = set()
    for i in pr:
        for j in dbl_sqr:
            found.add(i + j)
    for i in composite_odd:
        if i not in found:
            return i


if __name__ == '__main__':
    assert(primes_lt(10) == {2, 3, 5, 7})
    print(mark_under(10 ** 4))
