'''
This techincally works, but there is an analytic soltuion. Start with the
recurrence, and find the closed form by substituting a solution of the form
f=ab^n, and solving the quadratic for the roots. Then, set up an equation using
the log of the closed form and notice that one of the terms decreases
geometrically.
'''
from math import log10

if __name__ == '__main__':
    val = 1
    prev = 1
    idx = 2
    while log10(val) < 999:
        idx += 1
        nval = val + prev

        prev = val
        val = nval

        print(idx, log10(val))
    print('>', idx, val, log10(val))
