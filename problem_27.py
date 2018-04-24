def prime(n):
    """Returns True if n is prime."""
    if n < 2:
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
def quadratic_primes():
    ma = None
    mb = None
    mprimes = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            primes = 0
            n = 0
            f_isprime = True
            while f_isprime:
                f = n**2 + a * n + b
                f_isprime = prime(f)
                if f_isprime:
                    primes += 1
                    if primes > mprimes:
                        ma = a
                        mb = b
                        mprimes = primes
                n += 1
    return ma, mb
if __name__ == '__main__':
    a, b = quadratic_primes()
    print(a * b)
