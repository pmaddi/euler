from fractions import Fraction
import itertools

def conv(lst):
    if not lst:
        return None
    if len(lst) == 1:
        return Fraction(lst[0])
    return lst[0] + 1/conv(lst[1:])

def e_cont():
    yield 2
    i = 1
    k = 1
    while True:
        if i % 3 == 2:
            yield 2 * k
            k += 1
        else:
            yield 1
        i +=1

if __name__ == '__main__':
    ls = list(itertools.islice(e_cont(), 100))
    num = conv(ls).numerator
    print(sum([int(i) for i in str(num)]))
