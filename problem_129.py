'''
R(k) = k 1's
R(6) = 111111

n > 0
n is not multiple of 2 or 5. Coprime with 10.

R(k) is divisible by n

A(n) is the least such value of k

A(7) = 6
111111 is the smallest repunit that is a multiple of 7

For each n, find A(n).
Find A(n) by iterating up each R(k) to find the smallest one


1
10 + 1
100 + 10 + 1
11
111

Thinking about the factorizations of repunits?

Are there any patterns or recurrences that can be built from sucessive values of
R(k)?


Algorithim 1:
- For each prime number p, find A(p) by searching up sucessive R(k)'s and seeing
  if they are a multiple of p.

As an alternative, perhaps we can find A(p) by some form of modified long
division where we target repeated 1's as we go...

7*3 = 21

12
017
183
111

Algorithim 2:
- Keep a table of primes to A(p). For each R(k), find it's prime factorization.
  Add to the table p->k for each p in the factorization if p is not already in
  the table.
- I feel less good about this direction since factoring a million digit number
  feels hopeless.

Why isn't 1000171 it?
'''

def primes_lt(n):
    # too slow
    nums = [0] * (n - 1)
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

def ones_count(number):
    dividend = 1
    first = True
    count = 0
    while dividend:
        if not first:
            dividend += 1
        else:
            first = False
        count += 1
        dividend = (dividend % number) * 10
    return count

def test_ones_count():
    assert ones_count(7) == 6
    assert ones_count(41) == 5

if __name__ == '__main__':
    test_ones_count()
    # for i in range(1, 10000):
    #     if i in [1, 2, 5]:
    #         continue
    #     if i % 2 == 0 or i % 5 == 0:
    #         continue
    #     print(i, ones_count(i))
    msf = 1
    msfv = 1
    for prime in sorted(list(primes_lt(5000000))):
        if prime in [1, 2, 5]:
            continue
        if prime < 1000000 - 100:
            continue
        ocp = ones_count(prime)
        if ocp > msfv:
            msfv = ocp
            msf = prime
            print(msf, msfv)
        if msfv > 1000000:
            print("result", msf)
            break
