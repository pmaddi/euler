"""
For P(BB) = 1/2, where r is the number of red and b is the number of blue,

b / (r + b) * (b - 1) / (r + b - 1) = 1/2

must find where r + b > 10^12

numerator = b * (b-1) = b2 -b
denominator = (r+b)(r+b-1)=r2 + rb - r + rb + b2 -b = r2 + b2 + 2rb - r - b

find where 2b * (b - 1) = (r+b)(r+b-1)
2b2 - 2b = r2 + b2 + 2rb - r - b
0 = r2 + b2 + 2rb - r - b - (2b2 - 2b )
0 = r2 + b2 + 2rb - r - b - 2b2 + 2b
0 = r2 - b2 + 2rb - r + b

I threw this into wolfram alpha, and clicked the "Integer solutions."

Converted the plaintext versions into python.

Then, after running it, I realized that the formula for `b` was off by one!!!
No idea why that is.

"""
from math import sqrt

if __name__ == '__main__':
    n = 3
    while True:
        b = (2 + sqrt(2))/8 * ((3 - 2 * sqrt(2))**n + ((2 - sqrt(2))* (3 + 2 *
            sqrt(2))**n)/(2 + sqrt(2)) - 4/(2 + sqrt(2))
            ) + 1 # Mysterious plus one
        r = (-1) * ((3 - 2 * sqrt(2))**n + ((4 - 3 * sqrt(2))*(3 + 2 *
            sqrt(2))**n)/(4 + 3 * sqrt(2)))*(4 + 3 * sqrt(2))/8
        sm = b + r
        if b + r > 10**12:
            print(round(b))
            break
        n += 1
