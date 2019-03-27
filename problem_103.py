"""
Subsets cannot be equal
    Only 128 subsets to compare... brute force that?
Longer subset sums must be greater than shorter ones
    Ensure they're increasing, then make sure first 2 > last, first 3 > last 2,
    etc

Backtracking solution
"""
from itertools import combinations


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


def valid_range(parents):
    upper = min(parents)
    maxdffs = None
    for sp in range(len(parents) // 2):
        la = parents[:(sp + 1)]
        ra = parents[(-1 * (sp + 1)):]
        dff = sum(ra) - sum(la)
        if maxdffs is None or dff > maxdffs:
            maxdffs = dff
    if maxdffs is None:
        maxdffs = 0
    return range(maxdffs + 1, upper)


def test_valid_range():
    assert valid_range([9, 11, 12, 13]) == range(6, 9)
    assert valid_range([18, 19, 20, 22, 25]) == range(11, 18)


def h(parents, remaining, valid_range_fn=valid_range):
    """Returns the lowest sum sub-array satifying the constraints."""
    if not unequal_subsets(parents):
        return None
    if not remaining:
        return []
    minval = None
    for v in valid_range_fn(parents):
        sub = h([v] + parents, remaining - 1)
        if sub is None:
            continue
        sub_including_me = sub + [v]
        if minval is None or sum(sub_including_me) < sum(minval):
            minval = sub_including_me
    # print("h({}, {}) -> {}".format(parents, remaining, minval))
    return minval


def f(sz):
    M = 50
    return h([], sz, lambda x: range(1, M))


def test_f():
    assert f(1) == [1]
    assert f(2) == [1, 2]
    assert f(3) == [2, 3, 4]
    assert f(4) == [3, 5, 6, 7]
    assert f(5) == [6, 9, 11, 12, 13]
    assert f(6) == [11, 18, 19, 20, 22, 25]
    assert f(7) == [20, 31, 38, 39, 40, 42, 45]


if __name__ == '__main__':
    print(''.join([str(i) for i in f(7)]))
