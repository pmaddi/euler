'''
Prime can't fit the description because P(n) for prime n = n - 1

T(n) = prod(p - 1) for p in prime fac of n
T(p_1 *... p_n) = prod(p - 1)

n/T(n) = p_1 / (p_1 - 1) * p_2 / (p_2 - 1) *...


Final solution is mad slow.
'''
import numpy as np
from math import gcd
from itertools import product
from functools import reduce
import operator

N = 10
N = 10**6 + 1
N = 100000
N = 10**7

def primes_lt(n):
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

def totient(i):
    phi_c = 0
    for j in range(1, i):
        phi_c += int(gcd(i, j) == 1)
    return phi_c

def totient_from_prime_factorization(n, pf):
    s_pf = set(pf)
    out = n
    for v in s_pf:
        out *= (1 - 1/v)
    return int(out)

def pal(a, b):
    return sorted(str(a)) == sorted(str(b))

def products(len_range, primes):
    for r in len_range:
        for i in product(*(primes for i in range(r))):
            yield i
def main_1():
    assert(pal(87109, 79180))
    primes = primes_lt(N)

    msf = 10 ** 8
    msf_val = 0
    # for i in range(2, N):
    rev_primes = sorted(list(primes), reverse=True)
    # factorizations = products([1, 2], rev_primes)
    # factorizations = zip(rev_primes[3:], rev_primes[:-3])

    for power in range(2, 3):
        maxbase = N ** (1/power)
        filtered_primes = [p for p in rev_primes if p <= maxbase]

        # factorizations = zip(*(filtered_primes for _ in range(power)))
        for f_1 in filtered_primes:
            for f_2 in filtered_primes:
                fac = [f_1, f_2]
                num = reduce(operator.mul, fac, 1)
                if num > N:
                    continue
                phi_c = totient_from_prime_factorization(num, fac)
                if pal(phi_c , num):
                    rat = num/phi_c
                    if rat < msf:
                        msf = rat
                        msf_val = num
                    print(num, phi_c, rat, msf, msf_val)


if __name__ == '__main__':
    # print('### Making primes')
    primes = primes_lt(N)

    # print('### Making factorisations')
    factorizations = {}
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

    # print('### Finding min tot rat')
    msf = 10 ** 8
    msf_val = 0
    for basenum, fac in factorizations.items():
        num = reduce(operator.mul, fac, 1)
        if num > N:
            continue
        phi_c = totient_from_prime_factorization(num, fac)
        if pal(phi_c , num):
            rat = num/phi_c
            if rat < msf:
                msf = rat
                msf_val = num
    print(msf_val)
