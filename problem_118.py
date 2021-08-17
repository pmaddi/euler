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

def prime_count(numlist):
    perms = list(permutations(numlist, len(numlist)))
    cnt = 0
    for p in perms:
        v = int(''.join(p))
        pr = is_prime(v)
        if pr:
            cnt += 1
    return cnt

def waycount():
    combos = powerset('123456789')
    num_tuple_to_primes = {v: prime_count(v) for v in combos}
    cache = {p: {(p,)} for p, k in num_tuple_to_primes.items() if k > 0}
    cache[()] = {(())}
    last = None
    for c in combos:
        lst = set()
        c_set = set(c)
        used = set()
        for sub in powerset(c):
            used.add(sub)
            sub_set = set(sub)
            other = tuple(sorted(c_set - sub_set))
            if other in used:
                continue
            lhs = cache.get(sub, set())
            rhs = cache.get(other, set())
            for l in lhs:
                for r in rhs:
                    lst.add(tuple(sorted(l + r)))
        cache[c] = lst
        last = lst
    final_cnt = 0
    for sltn in last:
        prod = 1
        for val in sltn:
            prod *= num_tuple_to_primes[val]
        final_cnt += prod
    return final_cnt


if __name__ == '__main__':
    print(waycount())
