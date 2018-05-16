'''
T = n(n+1)/2

P = n(3n-1)/2
n = (1/2 +- squrt(1/4 - 4(3/2)(- pn))) / 3

H = n(2n-1)
0 = 2n^2 - n - H
n = (1 +- squrt(1 - 4*2*(-H))) / 4
'''
from problem_44 import real_inverse_pent, squrt, is_int

def real_inverse_hex(h):
    return (1 + squrt(1 - 4 * 2 * (-1 * h))) / 4

def generate_triangle():
    n = 1
    while True:
        T = n * (n + 1) / 2
        yield T
        n += 1

def do():
    for T in generate_triangle():
        if is_int(real_inverse_pent(T)):
            if is_int(real_inverse_hex(T)):
                if T > 40755:
                    return int(T)

if __name__ == '__main__':
    print(do())
