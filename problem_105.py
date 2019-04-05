from itertools import combinations
from pathlib import Path


def unequal_subsets(lst):
    st = set()
    for r in range(1, len(lst) + 1):
        for c in combinations(lst, r):
            sm = sum(c)
            if sm in st:
                return False
            else:
                st.add(sm)
    return True


def test_unequal_subsets():
    assert not unequal_subsets([1, 2, 3])
    assert unequal_subsets([])
    assert unequal_subsets([1])
    assert unequal_subsets([1, 2])
    assert unequal_subsets([2, 3, 4])
    assert unequal_subsets([3, 5, 6, 7])
    assert unequal_subsets([6, 9, 11, 12, 13])
    assert unequal_subsets([11, 18, 19, 20, 22, 25])


def h_larger_is_greater(lin, rin, lst):
    if rin >= lin:
        return False
    if not lst or len(lst) == 1:
        return True
    return h_larger_is_greater(lin + lst[0], rin + lst[-1], lst[1:-1])


def larger_is_greater(lst):
    if not lst:
        return True
    return h_larger_is_greater(lst[0], 0, lst[1:])


def test_larger_is_greater():
    assert not larger_is_greater([1, 2, 3])
    assert larger_is_greater([9, 11, 12, 13])
    assert not larger_is_greater([18, 19, 20, 22, 37])
    assert larger_is_greater([])
    assert larger_is_greater([1])
    assert larger_is_greater([1, 2])
    assert larger_is_greater([2, 3, 4])
    assert larger_is_greater([3, 5, 6, 7])
    assert larger_is_greater([6, 9, 11, 12, 13])
    assert larger_is_greater([11, 18, 19, 20, 22, 25])


if __name__ == '__main__':
    lns = [
        sorted([int(j) for j in i.split(',')])
        for i in
        Path('p105_sets.txt').read_text().split()
    ]
    out = 0
    for l in lns:
        if unequal_subsets(l) and larger_is_greater(l):
            out += sum(l)
    print(out)



