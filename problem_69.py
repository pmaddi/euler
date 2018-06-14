'''
# Too slow
from math import gcd

N = 10
N = 10**6 + 1

for i in range(2, N):
    phi_c = 0
    for j in range(1, i):
        phi_c += int(gcd(i, j) == 1)
    if i % (10**3) == 0:
        print(i, i / phi_c)
'''
import numpy as np
N = 11
N = 10**6 + 1
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

def prime_factor_set(n):
    i = 2
    out = set()
    while i ** 2 <= n:
        if n % i == 0:
            n = n // i
            out.add(i)
        else:
            i += 1
    if n > 1:
        out.add(n)
    return out

prime_factors = primes_lt(N)
prime_factor_divisible_by = {
        i: set()
        for i in prime_factors}

msf = 0
v_msf = 0

for val in range(2, N):
    pfs = prime_factor_set(val)
    non_relatively_prime_set = set()
    for prime in pfs:
        st = prime_factor_divisible_by[prime]
        st.add(val)
        non_relatively_prime_set = non_relatively_prime_set.union(st)


    phi = val-len(non_relatively_prime_set)
    rat = val / phi
    if rat > msf:
        msf = rat
        v_msf = val
        print(v_msf, msf)
