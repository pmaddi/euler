'''
3 4 5 6
cmp 3,4 6
cmp 3 4
cmp 4 5
cmp 5 6
You need to compare things that arent enforced by the increasing ordering and
more is greater!

prop: if a subset is unequal size, then we dont need to check (i)
prop: if subests are of size 1 then no need to check because strictly
increasing
if there's no "overlap", then no need to check

aabb
abba
abab -> not tested becuase each element of a has a strictly greater than in the
other set.

3678

Go through each of the subset pairs and check whether each elem has a strictly
greater than in the other set. If not, then needs to be checked.

'''

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
    assert (len(subsets(4))) == 25
    assert (len(subsets(7))) == 966
    assert (len(subsets(12))) == 261625


if __name__ == '__main__':
    print(subsets(4))
