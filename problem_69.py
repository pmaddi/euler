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
'''
import numpy as np
N = 101
N = 10**6 + 1
N = 211
def primes_lt(n):
    # too slow
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

primes = primes_lt(N)

factorizations = {}
# The prime factorization for each val
for i in primes:
    j = 1
    while True:
        val = i * j
        if val > N:
            break
        st = factorizations.get(val, set())
        st.add(i)
        factorizations[val] = st
        j += 1

# inverted_factorizations = {}
# # The numbers that have the prime in its prime factorization
# for i, st in factorizations.items():
#     for prime in st:
#         s = inverted_factorizations.get(prime, set())
#         s.add(i)
#         inverted_factorizations[prime] = s
#
#
# non_relatively_prime_under = {}
# # The numbers lower than key that are not relatively prime to it
# for num, primes in factorizations.items():
#     for p in primes:
#         relatives = inverted_factorizations[p]
#         for r in relatives:
#             if r >= num:
#                 s = non_relatively_prime_under.get(r, set())
#                 s.add(num)
#                 non_relatively_prime_under[r] = s
# print(len(non_relatively_prime_under))






prime_factor_divisible_by = {
        i: set()
        for i in primes }
msf = 0
v_msf = 0

for val in range(2, N):
    pfs = factorizations[val]
    non_relatively_prime_set = set()
    for prime in pfs:
        st = prime_factor_divisible_by[prime]
        st.add(val)
        non_relatively_prime_set = non_relatively_prime_set.union(st)
    phi = val-len(non_relatively_prime_set)
    rat = val / phi
    print('>>>', val, len(pfs), rat)
    # if val % (10**3) == 0:
    #     print('>>>', val, len(pfs), rat)
    if rat > msf:
        msf = rat
        v_msf = val
        print(v_msf, msf)
'''
import numpy as np
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
if __name__ == '__main__':
    primes = sorted(list(primes_lt(N)))
    val = 1
    for p in primes:
        val_new = p * val
        if val_new > N:
            print(val)
            break
        else:
            val = val_new
