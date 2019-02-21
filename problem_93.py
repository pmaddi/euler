'''Pretty slow, but under a minute'''
from fractions import Fraction

OPERATIONS = [
    lambda x, y: x * y,
    lambda x, y: Fraction(x, y),
    lambda x, y: x - y,
    lambda x, y: x + y,
]

def diff(it1, it2):
    return tuple(sorted(tuple(set(it1) - set(it2))))

def expr_h(length, using):
    '''Finds the producable values.

    @length: the number of digits that should be consumed
    @using: the available numbers. a sorted tuple.

    returns ((producable_value, (used_number, ...), ...)
    '''
    if length == 1:
        out = tuple((u, (u,)) for u in using)
    else:
        options = ()
        for lhs_length in range(1, length):
            lhs = expr_h(lhs_length, using)
            for l_produced, l_used in lhs:
                available_values = diff(using, l_used)
                rhs = expr_h(length - lhs_length, available_values)
                for r_produced, r_used in rhs:
                    for op in OPERATIONS:
                        try:
                            options += (
                                (op(l_produced, r_produced), l_used + r_used),
                            )
                        except ZeroDivisionError:
                            pass
        out = tuple(sorted(options, key=lambda x: x[0]))
    return out

def expr(using):
    '''Using is a sorted tuple'''
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
