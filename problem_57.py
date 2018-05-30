from fractions import Fraction

if __name__ == '__main__':
    f = Fraction(2)
    count = 0
    out = []
    for i in range(1, 1001):
        e = 1 + 1/f
        if len(str(e.numerator)) > len(str(e.denominator)):
            count += 1
        out.append(e)
        print(count, i)
        f = 2 + 1/f
