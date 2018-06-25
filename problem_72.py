'''
def farey_function(n, descending=False):
    """
    Wikipedia
    Print the nth Farey sequence, either ascending or descending.
    """
    a, b, c, d = 0, 1, 1, n
    if descending:
        a, c = 1, n-1
    yield a,b
    while (c <= n and not descending) or (a > 0 and descending):
        k = int((n + b) / d)
        a, b, c, d = c, d, (k*c-a), (k*d-b)
        yield a,b

print(len(list(farey_function(10**6)))-2)
'''
import numpy as np

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

def all_factorizations_lt(n, primes):
    factorizations = {}
    # The prime factorization for each val
    for i in primes:
        j = 1
        while True:
            val = i * j
            if val > n:
                break
            st = factorizations.get(val, set())
            st.add(i)
            factorizations[val] = st
            j += 1
    return factorizations

def totient_from_prime_factorization(n, pf):
    s_pf = set(pf)
    out = n
    for v in s_pf:
        out *= (1 - 1/v)
    return int(out)

def cnt(n):
    primes = primes_lt(n)
    all_factorizations = all_factorizations_lt(n, primes)
    out = 0
    for i in range(2, n + 1):
        factorization = all_factorizations[i]
        out += totient_from_prime_factorization(i, factorization)
    return out

if __name__ == '__main__':
    assert(cnt(8) == 21)
    print(cnt(10**6))
