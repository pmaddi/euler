from itertools import permutations
from math import sqrt


def is_prime(x):
    if x <= 1:
        return False
    if x % 2 == 0 and x > 2:
        return False
    for i in range(3, int(sqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

def test_is_prime():
    assert is_prime(2)
    assert is_prime(1117)
    assert not is_prime(4)
    assert not is_prime(1111)

def find_none(lst):
    try:
        return lst.index(None)
    except ValueError:
        return None

def to_int(lst):
    return sum(
            val * (10 ** idx)
            for (idx, val)
            in enumerate(reversed(lst)))

def test_to_int():
    assert to_int([1, 1, 1]) == 111
    assert to_int([0, 1, 1]) == 11
    assert to_int([0, 1, 0]) == 10
    assert to_int([0, 2, 1, 0]) == 210

def ways(n_digit, repeats, digit):
    base = [digit] * repeats + [None] * (n_digit - repeats)
    candidates = []
    blanked = set(permutations(base, n_digit))
    not_done = list(blanked)
    options = [i for i in range(10) if i != digit]
    while not_done:
        val = not_done.pop(0)
        none_idx = find_none(val)
        if none_idx is None:
            candidates.append(val)
            continue
        for option in options:
            new = list(val[:])
            new[none_idx] = option
            not_done.append(new)
    for cand in candidates:
        int_can = to_int(cand)
        if int_can > 10**(n_digit - 1) and is_prime(int_can):
            yield int_can

def sum_s(n_digit):
    out = 0
    for d in range(10):
        candidate_m = n_digit - 1
        while True:
            assert candidate_m > 0
            w = list(ways(n_digit, candidate_m, d))
            if len(w) > 0:
                sm = sum(w)
                # le = len(w)
                # print(n_digit, d, candidate_m, le, sm)
                out += sm
                break
            candidate_m -= 1
    return out

if __name__ == '__main__':
    print(sum_s(10))
