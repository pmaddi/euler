import numpy as np
import math


def rotations(n):
    digits = int(math.log10(n)) + 1
    for i in range(digits):
        leading = n // (10  **  (digits - 1))
        n = (n % (10  **  (digits - 1))) * 10 + leading
        yield n

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
    out = []
    for i in primes:
        if all([j in primes for j in rotations(i)]):
            out.append(i)
    return out

if __name__ == '__main__':
    assert(list(rotations(123)) == [231, 312, 123])
    print(len(primes_lt(10 ** 6)))
