from fractions import Fraction

def fracs_lt(v, max_denom):
    for i in range(1, max_denom + 1):
        n = int(i * v)
        f = Fraction(n, i)
        if f < v:
            yield f
if __name__ == '__main__':
    print(max(fracs_lt(Fraction(3,7), 10**6)).numerator)
