'''
Maybe do some some kind of binary search?

# Dont work
from itertools import permutations, product
from math import ceil, floor

def rnd(fl):
    eps = .0001
    if ceil(fl) - fl < eps:
        return ceil(fl)
    elif fl - floor(fl) < eps:
        return floor(fl)
    return fl

def test_round():
    assert rnd(1) == 1
    assert rnd(1.000001) == 1
    assert rnd(.9999999) == 1
    assert rnd(.8999999) == .8999999
    assert rnd(.559999) == .559999

def translate(op_string):
    tbl = {
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            '-': lambda x, y: x - y,
            '+': lambda x, y: x + y,
    }
    return tbl[op_string]

def count(digits):
    expressable = set()
    if len(set(digits)) != 4:
        print(digits)
        assert False
    # add to expressable nums
    digit_perms = list(permutations(digits, 4))
    op_combs = list(product('*/+-', repeat=3))
    for op_set in op_combs:
        for digit_set in digit_perms:
            try:
                # a + b + c + d
                val0 = translate(op_set[0])(digit_set[0], digit_set[1])
                val1 = translate(op_set[1])(val0, digit_set[2])
                val2 = translate(op_set[2])(val1, digit_set[3])
            except ZeroDivisionError:
                pass
            else:
                expressable.add(rnd(val2))
            try:
                # (a + b) + (c + d)
                vall = translate(op_set[0])(digit_set[0], digit_set[1])
                valr = translate(op_set[2])(digit_set[2], digit_set[3])
                val2 = translate(op_set[1])(vall, valr)
            except ZeroDivisionError:
                pass
            else:
                expressable.add(rnd(val2))
            try:
                # a + (b + c) + d
                valp = translate(op_set[1])(digit_set[1], digit_set[2])
                vall = translate(op_set[0])(digit_set[0], valp)
                val2 = translate(op_set[2])(valp, val1)
            except ZeroDivisionError:
                pass
            else:
                expressable.add(rnd(val2))
            try:
                # a + b + (c + d)
                valp = translate(op_set[2])(digit_set[2], digit_set[3])
                vall = translate(op_set[0])(digit_set[0], digit_set[1])
                val2 = translate(op_set[1])(valp, val1)
            except ZeroDivisionError:
                pass
            else:
                expressable.add(rnd(val2))
            try:
                # a + (b + c + d)
                val1 = translate(op_set[1])(digit_set[1], digit_set[2])
                valr = translate(op_set[2])(val1, digit_set[3])
                val2 = translate(op_set[0])(digit_set[0], valr)
            except ZeroDivisionError:
                pass
            else:
                expressable.add(rnd(val2))
            try:
                # a + (b + (c + d))
                valrr = translate(op_set[2])(digit_set[2], digit_set[3])
                val1 = translate(op_set[1])(digit_set[1], valrr)
                val2 = translate(op_set[0])(digit_set[0], val1)
            except ZeroDivisionError:
                pass
            else:
                expressable.add(rnd(val2))
            try:
                # (a + (b + c)) + d
                valr = translate(op_set[1])(digit_set[1], digit_set[2])
                val1 = translate(op_set[0])(digit_set[0], valr)
                val2 = translate(op_set[2])(val1, digit_set[3])
            except ZeroDivisionError:
                pass
            else:
                expressable.add(rnd(val2))
            # print(digit_set, op_set, val2)
    # count contiguous from 1 to N
    # print(sorted(list(expressable)))
    i = 1
    while True:
        if i not in expressable:
            break
        i += 1
    return i - 1

def find_max():
    msf = ''
    msf_v = 0
    for a in range(10):
        for b in range(a + 1, 10):
            for c in range(b + 1, 10):
                for d in range(c + 1, 10):
                    cnt = count((a, b, c, d))
                    # print((a,b,c,d), cnt,  msf_v, msf)
                    if cnt > msf_v:
                        msf_v = cnt
                        msf = f"{a}{b}{c}{d}"
    print(msf_v, msf)
    return msf

def test_count():
    assert count((1, 2, 3, 4)) == 28

if __name__ == '__main__':
    #count((1, 2, 3, 4))
    print(find_max())
'''

from fractions import Fraction

# Do something like creating expressions of length n and producing all
# expressions of length n up to that size...

OPERATIONS = [
    lambda x, y: x * y,
    lambda x, y: Fraction(x, y),
    lambda x, y: x - y,
    lambda x, y: x + y,
]

def diff(it1, it2):
    return tuple(set(it1) - set(it2))

def expr_h(length, using):
    '''Finds the producable values.

    @length: the number of digits that should be consumed
    @using: the available numbers

    returns [(producable_value, (used_number, ...)]
    '''
    if length == 1:
        return [(u, (u,)) for u in using]
    else:
        options = []
        for lhs_length in range(1, length):
            lhs = expr_h(lhs_length, using)
            for l_produced, l_used in lhs:
                assert(len(l_used) == lhs_length)
                available_values = diff(using, l_used)
                assert(available_values)
                rhs = expr_h(length - lhs_length, available_values)
                for r_produced, r_used in rhs:
                    for op in OPERATIONS:
                        try:
                            options.append(
                                (op(l_produced, r_produced), l_used + r_used)
                            )
                        except ZeroDivisionError:
                            pass
        options.sort(key=lambda x: x[0])
        return options

def expr(using):
    return set(i for i, j in expr_h(len(using), using))

def continuous(st):
    i = 1
    while True:
        if i not in st:
            return i - 1
        i += 1

def find_max():
    msf = ''
    msf_v = 0
    for a in range(10):
        for b in range(a + 1, 10):
            for c in range(b + 1, 10):
                for d in range(c + 1, 10):
                    cnt = continuous(expr((a, b, c, d)))
                    if cnt > msf_v:
                        msf_v = cnt
                        msf = f"{a}{b}{c}{d}"
    return msf

if __name__ == '__main__':
    print(find_max())
