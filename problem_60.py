'''
I DIDNT MAKE THIS
my fave solution from the forums
'''
from itertools import permutations
from math import sqrt

cache = {}
cnt = [0]
def is_prime(x):
  cnt[0] += 1
  if x <= 1:
    return False
  if x % 2 == 0 and x > 2:
    return False
  for i in range(3, int(sqrt(x)) + 1, 2):
    if x % i == 0:
      return False
  return True

def prime_sieve(limit):
  a = [True] * limit
  a[0] = a[1] = False
  for i, is_prime in enumerate(a):
    if is_prime:
      yield i
      for n in range(i**2, limit, i):
        a[n] = False

def is_pair(a, b):
  if (a, b) not in cache:
    cache[(a, b)] = all(is_prime(x) for x in [int(''.join(x)) for x in permutations([str(a), str(b)], 2)])
  return cache[(a, b)]

primes = list(prime_sieve(10000))

def main():
  for a in primes:
    for b in primes:
      if a > b:
        continue
      if is_pair(a, b):
        for c in primes:
          if b > c:
            continue
          if is_pair(a, c) and is_pair(b, c):
            for d in primes:
              if c > d:
                continue
              if is_pair(a, d) and is_pair(b, d) and is_pair(c, d):
                for e in primes:
                  if d > e:
                    continue
                  if is_pair(a, e) and is_pair(b, e) and is_pair(c, e) and is_pair(d, e):
                    print(cnt[0])
                    return a+b+c+d+e

if __name__ == '__main__':
    print(main())
