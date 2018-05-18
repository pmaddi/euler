import logging
FACTORIZATION_CACHE = {}
def t_sorted(*args):
    return tuple(sorted(*args))

def factorization(n):
    if n in {1,2,3,5,7,11}:
        FACTORIZATION_CACHE[n] = (n,)
        return (n,)
    if n in FACTORIZATION_CACHE:
        return FACTORIZATION_CACHE[n]
    for i in range(2, n):
       if n % i == 0:
            ret = t_sorted(factorization(i) + factorization(int(n / i)))
            FACTORIZATION_CACHE[n] = ret
            return ret
    FACTORIZATION_CACHE[n] = (n,)
    return (n,)

def n_distinct_n_consecutive(n):
    i = 1
    sofar = 0
    first_sofar = 0
    while True:
        cnt = len(set(factorization(i)))
        if cnt == n:
            if sofar == 0:
                first_sofar = i
            sofar += 1
        else:
            sofar = 0
        if sofar == n:
            return first_sofar
        i += 1

def v1_main():
    '''
    Works but takes 1m36s
    '''
    assert(factorization(644) == (2, 2, 7, 23))
    assert(factorization(644) == (2, 2, 7, 23))
    assert(factorization(646) == (2, 17, 19))
    assert(n_distinct_n_consecutive(2) == 14)
    assert(n_distinct_n_consecutive(3) == 644)
    print(n_distinct_n_consecutive(4))


import numpy as np
from collections import defaultdict

def prime_factors(n):
    '''too slow'''
    nums = defaultdict(lambda: 0)#np.zeros(n - 1)
    nums[1] = 1
    for i in range(2, n):
        if nums[i] == 0:
            for j in range(2, (n // i) + 1):
                if i * j < n:
                    nums[i * j] = nums[i * j] + 1 # is nonprime
    return nums

def find_cnt(n, limit=10**7):
    pf = prime_factors(limit)
    for i in range(1, limit):
        b = True
        for j in range(n):
            b = b and (pf[i + j] == n)
        if b:
            return i

def v2_main():
    '''
    takes 1.6 s
    '''
    assert(find_cnt(2, limit=30) == 14)
    assert(find_cnt(3, limit=10**3) == 644)
    print(find_cnt(4, limit=10**6))

if __name__ == '__main__':
    v2_main()
