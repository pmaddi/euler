from math import sqrt
from itertools import permutations, combinations

def prime_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for i, is_prime in enumerate(a):
        if is_prime:
            stri = str(i)
            if len(stri) == len(set(str(i))):
                yield i
            for n in range(i**2, limit, i):
                a[n] = False

def is_prime(x):
    if x <= 1:
        return False
    if x % 2 == 0 and x > 2:
        return False
    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

def powerset(lst):
    out = []
    for i in range(1, 10):
        out += list(combinations(lst, i))
    return out

def has_prime(numlist):
    perms = list(permutations(numlist, len(numlist)))
    for p in perms:
        v = int(''.join(p))
        pr = is_prime(v)
        if pr:
            return True
    return False

def waycount():
    combos = powerset('123456789')
    primes = [v for v in combos if has_prime(v)]
    cache = {p: 1 for p in primes}
    cache[()] = 1
    for c in combos:
        count = 0
        c_set = set(c)
        used = set()
        for sub in powerset(c):
            used.add(sub)
            sub_set = set(sub)
            other = tuple(sorted(c_set - sub_set))
            if other in used:
                continue
            count += cache.get(sub, 0) * cache.get(other, 0)
        cache[c] = count
        print(c, count)

if __name__ == '__main__':
    waycount()
