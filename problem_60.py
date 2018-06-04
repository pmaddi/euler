import numpy as np
import math

EXP = 6
MAXVAL = 10**EXP

def digits(x):
    return int(math.log10(x)) + 1

def concat(i, j):
    return int(str(i) + str(j))

def isprime(n):
    """Returns True if n is prime."""
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def primes_lt(n):
    '''too slow'''
    nums = np.zeros(n - 1, dtype=bool)
    nums[0] = True
    for i in range(2, int(n ** .5) + 1):
        if nums[i - 1] == True:
            continue
        for j in range(2, (n // i) + 1):
            if i * j < n:
                nums[i * j - 1] = True # is nonprime
    for i in range(len(nums)):
        if not nums[i]:
            yield i + 1

def primes_lt_alt(n):
    '''too slow'''
    nums = np.zeros(n - 1, dtype=bool)
    nums[0] = True
    m = int(n ** .5)
    for i in range(2, n):
        if nums[i - 1] == True:
            continue
        else:
            yield i
        if i > m:
            continue
        for j in range(2, (n // i) + 1):
            if i * j < n:
                nums[i * j - 1] = True # is nonprime

def ts(*i):
    return tuple(sorted(i))

def valid(p_i, p_j, p_set):
    return concat(p_i, p_j) in p_set and concat(p_j, p_i) in p_set

def explore(v, trie):
    if (v not in trie) and (not isprime(v)):
        return
    for k in trie:
        pos1 = concat(k, v)
        pos2 = concat(v, k)

    if v in trie:
if __name__ == '__main__':
    TRIE = {}
    t = TRIE
    i = 1
    while True:
        if i in t:
            i += 1
            continue
        if isprime(i):
            t[i] = {}
            i += 1
            continue
        i += 1



