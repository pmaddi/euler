import numpy as np
from itertools import combinations

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

COUNTS = {}
PRIMES = primes_lt(10**4 + 1)

def valid_diffs(lst):
    for c in combinations(lst, 3):
        if h_valid_diffs(c):
            return c

def h_valid_diffs(lst):
    lst = sorted(lst)
    last_diff = None
    last = None
    for i in lst:
        if last is not None:
            df = i - last
            if last_diff is not None:
                if last_diff != df:
                    return False
            last_diff = df
        last = i
    return True

def cjoin(it):
    return int(''.join([str(i) for i in sorted(it)]))

def main():
    for i in range(10**3, 10**4 + 1):
        if i in PRIMES:
            key = int(''.join(sorted(str(i))))
            ls = COUNTS.get(key, []) + [i]
            COUNTS[key] = ls
    COUNTS_3 = {i: j for i, j in COUNTS.items() if len(j) >= 3}
    COUNTS_VALID = {
        i: cjoin(valid_diffs(j))
        for i, j in COUNTS_3.items()
        if valid_diffs(j) is not None}
    print(COUNTS_VALID)

if __name__ == '__main__':
    assert(valid_diffs([1,2,3]))
    assert(not valid_diffs([1,2,4]))
    assert(valid_diffs([1487, 4817, 8147]))
    main()
