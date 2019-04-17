from itertools import combinations, chain


def powerset(lst):
    return chain(*(combinations(lst, i) for i in range(1, len(lst) + 1)))


def g_subsets(n):
    vals = list(range(n))
    a_vals = powerset(vals)
    seen = set()
    for a in a_vals:
        for b in powerset(sorted(list(set(vals) - set(a)))):
            if (a, b) not in seen and (b, a) not in seen:
                seen.add((a, b))
                yield (a, b)


def subsets(n):
    return list(g_subsets(n))


def test_subsets():
    assert len(subsets(4)) == 25
    assert len(subsets(7)) == 966
    assert len(subsets(12)) == 261625


def check(a, b):
    '''Whether it needs to be checked.'''
    if len(a) != len(b):
        return False
    if len(a) == 1:
        return False
    if a[0] > b[0]:
        gr = a
        le = b
    else:
        gr = b
        le = a
    # If all the lt values are covered by a greater value, don't check. But if
    # one if them is covered, must check.
    for idx in range(len(le)):
        if le[idx] >= gr[idx]:
            return True
    return False


def test_check():
    assert check([0, 3], [1, 2])
    assert check([1, 2], [0, 3])
    assert not check([0, 1], [2, 3])
    assert not check([0, 2], [1, 3])
    assert not check([1, 3], [0, 2])
    assert not check([0], [1])
    assert not check([2], [1, 2])


def checks_needed(n):
    cnt = 0
    for a, b in subsets(n):
        if check(a, b):
            cnt += 1
    return cnt


def test_checks_needed():
    assert checks_needed(4) == 1
    assert checks_needed(7) == 70


if __name__ == '__main__':
    print(checks_needed(12))
