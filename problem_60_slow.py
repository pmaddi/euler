import numpy as np
import math

EXP = 8
MAXVAL = 10**EXP

def digits(x):
    return int(math.log10(x)) + 1

def concat(i, j):
    return int(str(i) + str(j))

# def isprime(n, pset):
#     if n in pset:
#         return True
#     v = h_isprime(n)


def isprime(n):
    """Returns True if n is prime."""
    if n == 1:
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

def primes_lt(n):
    '''too slow'''
    nums = np.zeros(n - 1, dtype=bool)
    nums[0] = True
    for i in range(2, int(n ** .5) + 1):
        if nums[i - 1] == True:
            continue
        for j in range(2, (n // i) + 1):
            if i * j < n:
                nums[i * j - 1] = True # is nonprime
    for i in range(len(nums)):
        if not nums[i]:
            yield i + 1

def ts(*i):
    return tuple(sorted(i))

def valid(p_i, p_j, p_set):
    return concat(p_i, p_j) in p_set and concat(p_j, p_i) in p_set

if __name__ == '__main__':
    primes = list(primes_lt(MAXVAL))
    p_set = set(primes)
    pairs = set()

    for i in range(len(primes)):
        p_i = primes[i]
        if p_i > 10**(EXP // 2):
            break
        for j in range(i, len(primes)):
            p_j = primes[j]
            if digits(concat(p_i, p_j)) > EXP:
                break
            # if concat(p_i, p_j) > MAXVAL:
            #     if not (isprime(concat(p_i, p_j)) and isprime(concat(p_j, p_i))):
            #         continue
            if valid(p_i, p_j, p_set):
                pairs.add(ts(p_i, p_j))
            # maxcat = max(concat(p_i, p_j), concat(p_j, p_i))
            # if maxcat < MAXVAL:
            #     continue
            # if isprime(concat(p_i, p_j)) and isprime(concat(p_j, p_j)):
            #     pairs.add(ts(p_i, p_j))

    lenthing = 3
    new_store = None
    old_store = list(pairs)
    for x in range(3, 6):
        old_store_primes = sorted(list(set([i for j in old_store for i in j])))
        new_store = set()
        for i in range(len(old_store_primes)):
            p_i = old_store_primes[i]
            if p_i > 10**(EXP // 2):
                break
            for j in range(len(old_store)):
                p_j = old_store[j]
                does = True
                for v in p_j:
                    # if digits(concat(p_i, v)) == EXP + 1 or digits(concat(p_i, v)) == EXP + 2:
                    #     if not (isprime(concat(p_i, v)) and isprime(concat(v, p_i))):
                    #         does = False
                    #         continue
                    if not valid(p_i, v, p_set):
                        does = False
                        continue
                if does:
                    new_store.add(ts(p_i, *p_j))
        old_store = list(new_store)
    print(sum(list(new_store)[0]))
