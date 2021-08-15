from functools import reduce
from problem_60 import prime_sieve

def solutions4(n, pr=False):
    count = 0
    for d in range(1, n + 1):
        if n ** 2 % d == 0:
            count += 1
    return count

def test_solutions():
    fn = solutions4
    assert fn(4) == 3
    assert fn(1260) == 113

def findmt():
    v = 1
    while True:
        s = solutions4(v)
        if s == 11:
            s = solutions4(v, True)
            print(">>> v, s", v, s)
        # print(">>> v, s", v, s)
        if v > 60:
            return s
        v += 1

# What is the smallest n such that n^2 has gt 4M divisors less than n?
# num divisors of n^2 less than n is num divisors of n^2 plus 1 div 2.
# num divisors of n^2 is
# Get the number or divisors of a prime factorixation.
def divisors(pmf):
    primes = set(pmf)
    out = 1
    for p in primes:
        out = out * (len([i for i in pmf if i == p]) + 1)
    return out

def test_cbf():
    assert divisors([2, 2, 2, 2])  == 5

def solutions_pmf(pmf):
    sqed = pmf + pmf
    return (divisors(sqed) + 1) / 2

def test_sol_pmf():
    assert solutions_pmf([2, 2, 3, 3, 5, 7]) == 113

def tot(pmf):
    return reduce(lambda x, y: x * y, pmf)

def nxt(pmf):
    sq = (tot(pmf)) ** 2
    i = 1
    while sq % i == 0:
        i += 1
    return i

def bfs(target):
    primes = set(prime_sieve(50))
    cache = set()
    msf_fac = []
    msf_total  = None
    msf_solutions = 0
    queue = [[2]]
    while len(queue):
        fac = queue.pop(0)
        fac = tuple(sorted(fac))
        if fac in cache:
            continue
        if len(fac) > 100:
            continue
        solutions = solutions_pmf(fac)
        total = tot(fac)
        cache.add(fac)
        if msf_total is not None and total > msf_total:
            continue
        if solutions > target:
            if msf_total is None or total < msf_total:
                msf_total = total
                msf_fac = fac
                msf_solutions = solutions
                print(msf_total, msf_fac, msf_solutions)
        else:
            least = sorted(list(primes - set(fac)))[0]
            for p in fac + (least,):
                queue.append(tuple(fac + (p,)))

# Took 5 mins to find 9350130049860600
if __name__ == '__main__':
    bfs(4000000)
