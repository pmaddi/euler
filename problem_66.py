'''
Too slow

def issquare(x):
    if not float(x).is_integer():
        return False
    n = int(x ** 0.5)
    return n ** 2 == x

out = []
for d in range(2, 100):
    if issquare(d):
        out.append((d, -1))
        continue
    x = 2
    while True:
        v = (x ** 2 - 1) / d
        if not x % 10**4:
            print(d, x, v)
        if issquare(v):
            out.append((d, x))
            break
        x += 1

print(out)
'''

from math import sqrt
from fractions import Fraction

def issquare(x):
    if not float(x).is_integer():
        return False
    n = int(x ** 0.5)
    return n ** 2 == x

def conv(lst):
    if not lst:
        return
    if len(lst) == 1:
        return Fraction(lst[0])
    return lst[0] + 1/conv(lst[1:])

def rep(v):
    s = sqrt(v)
    initial = int(s)
    digits = [initial]
    last_div = 1
    last_top_right = -1 * initial
    for idx in range(1, 10**7):
        frac = conv(digits)
        if (frac.numerator ** 2 - 1) == v * (frac.denominator)**2:
            return frac.numerator
        tmp_bottom = v - last_top_right ** 2
        assert(tmp_bottom / last_div == tmp_bottom // last_div)
        last_div = tmp_bottom // last_div
        if last_div == 0:
            return []
        val = int((s + -1 * last_top_right) / last_div)
        digits.append(val)
        last_top_right = -1 * last_top_right - last_div * val
    raise Exception('Couldnt find repeating for {}'.format(v))

def main():
    msf = 0
    max_d = 0

    for d in range(2, 1000):
        if issquare(d):
            continue
        cur = rep(d)
        if cur > msf:
            msf = cur
            max_d = d

    return (max_d, msf)

if __name__ == '__main__':
    print(main())
