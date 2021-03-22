import numpy as np


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

# Iterative Function to calculate
# (x^y)%p in O(log y)
def power(x, y, p) :
    res = 1     # Initialize result
    # Update x if it is more
    # than or equal to p
    x = x % p
    if (x == 0) :
        return 0
    while (y > 0) :
        # If y is odd, multiply
        # x with result
        if ((y & 1) == 1) :
            res = (res * x) % p
        # y must be even now
        y = y >> 1      # y = y/2
        x = (x * x) % p
    return res

def least_n_remainder_exceeding(min_remainder):
    approx_base_prime = round(min_remainder ** .5) * 10
    primes = sorted(primes_lt(approx_base_prime))
    for idx, prime in enumerate(primes):
        n = idx + 1
        ps = prime ** 2
        val = (power(prime - 1, n, ps) + power(prime + 1, n, ps)) % ps
        if val > min_remainder:
            return n

def test_ln():
    assert least_n_remainder_exceeding(10**9) == 7037


if __name__ == '__main__':
    print(least_n_remainder_exceeding(10**10))
