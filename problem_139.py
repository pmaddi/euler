"""
Note the most efficient but works.

The fast version noticies that all the primitives differ by one, and then
generates the next one using a recurrence.
"""
from math import gcd


def coun(limit):
    out = 0
    n = 1
    m = 2
    while 2 * m ** 2 + (2 * m * n) < limit:
        while 2 * m ** 2 + (2 * m * n) < limit:
            if gcd(m, n) == 1 and (m % 2 == 0 or n % 2 == 0):
                c = n ** 2 + m ** 2
                a = m ** 2 - n ** 2
                b = 2 * n * m
                if c % abs(a - b) == 0:
                    repetitions = limit // (a + b + c)
                    out += repetitions
                    print(a, b, c, repetitions, out)
            m += 1
        n += 1
        m = n + 1
    return out


if __name__ == '__main__':
    # print(coun(40))
    print(coun(100000000))
