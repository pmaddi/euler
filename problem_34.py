'''
Not a good solution.

The best version is to write out the sum of factorials vs the digits to
establish bounds

Also, it is better to look all the combinations of digits with replacement
rather than all the numbers till 10^7 because then you aren't checking the same
sum multiple times
'''
import math
FAC = {}
def factorial(n):
    assert(n < 10)
    if n == 0 or n == 1:
        return 1
    if FAC.get(n) is not None:
        return FAC.get(n)
    else:
        nex = n * factorial(n - 1)
        FAC[n] = nex
        return nex

def digits(n):
    d = math.log10(n)
    for i in range(int(d) + 1):
        yield (n // (10 ** i)) % 10

if __name__ == '__main__':
    out = []
    for i in range(1, 10 ** 7):
        s = 0
        for d in digits(i):
            s += factorial(d)
        if i == s:
            out.append(i)
            print(out)
    print(sum(out))





