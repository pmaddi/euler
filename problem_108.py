"""
1/a + 1/b = 1/n
1 + a/b = a/n
b + a = ab/n
bn + an = ab
(a + b)n = ab

Naiieve: Grid search through a and b, adding to buckets of n if they fall in.

What is the least value of n for which the number of distinct solutions exceeds
one-thousand?


1/5 + 1/20 = 1/4
4/20 + 1/20 = 5/20

1/6 + 1/12 = 1/4
2/12 + 1/12 = 1/4 = 3/12

1/8 + 1/8 = 2/8 = 1/4

1/4
2/8   -> 1/8,  1/8
3/12  -> 1/12, 2/12=1/6
4/16  -> 1/16, 3/16 dnr
5/20  -> 1/20, 4/20=1/5
6/24  -> 1/24, 5/24 nr
7/28  -> 1/28, 6/28=3/14
8/32  -> 1/32, 7/32
9/36  -> 1/36, 7/36
10/40 -> 1/40, 9/40

if __name__ == '__main__':
    MAX = 1000
    TRESH = 100
    cnts = {}
    for a in range(1, MAX):
        for b in range(a, MAX):
            prod = a * b
            sm = a + b
            if prod % sm != 0:
                continue
            dv = prod // sm
            cnts[dv] = cnts.get(dv, 0) + 1
    for idx, cnt in sorted(cnts.items(), key=lambda x: x[0]):
        if cnt > TRESH:
            print(idx)
    print(cnts)



1/n
1/x + 1/y
i/xi + j/yj = 1/n
where xi | n and yj | n

answer greater than 133945
answer less than 360360

1660
1800 4200'


for all solutions, lcm of i, j must divide n


1/n = 1/i + 1/j
1/n = (i + j)/ij
n = ij/(i + j)

How many pairs for which prod to sum ratio is n?
"""


def is_int(flt):
    eps = 1e-5
    err = abs(round(flt) - flt)
    return err < eps


def test_is_int():
    assert is_int(3)
    assert is_int(3.00000001)
    assert is_int(2.99999999)
    assert not is_int(3.0001)
    assert not is_int(3000.999)


def inv(cand, n):
    return 1 / (1 / n - 1 / cand)


def solutions_old(n):
    count = 0
    cand = n + 1
    while True:
        y = inv(cand, n)
        print(n, cand, y, is_int(y))
        if y < cand:
            return count
        if is_int(y):
            count += 1
        cand += 1


def solutions(n):
    count = 0
    for i in range(2, n + 2):
        count += ((n * i) % (i - 1) == 0)
    return count


def solution_st_1(n):
    count = 0
    out = []
    for i in range(2, n + 2):
        if (n * i) % (i - 1) == 0:
            count += 1
            out.append((n * i, inv(n * i, n)))
    return out


def solution_set(n):
    out = []
    cand = n + 1
    while True:
        y = inv(cand, n)
        # print(n, cand, y, is_int(y))
        if y < cand:
            return out
        if is_int(y):
            out.append((cand, round(y)))
        cand += 1

def solutions(n):
    """
    1/15 + 1/30 == 1/15(1/1 + 1/2) == 1/15(2/2 + 1/2) == 1/15(3/2) ==
    1/5*1/3(3/2) == 1/5*1/2 == 1/10

    1/7*1/2+1/7*1/5 == 1/7(1/2 + 1/5) == 1/7(5/10 + 2/10) == 1/7(7/10) ==
    1/10
    """
    count = 0
    cand = n + 1
    while True:
        y = inv(cand, n)
        print(n, cand, y, is_int(y))
        if y < cand:
            return count
        if is_int(y):
            count += 1
        cand += 1

def test_solutions():
    assert solutions(4) == 3
    assert solutions(1260) == 113


def find():
    n = 4
    while True:
        s = solutions(n)
        print(n, s)
        if s > 1000:
            return n
        n += 1

def find2():
    cnts = {}
    i = 1
    while True:
        for j in range(1, i + 1):
            prod = i * j
            sm = i + j
            if prod % sm != 0:
                continue
            val = i * j // (i + j)
            cnts[val] = cnts.get(val, 0) + 1
            print(i, j, val, cnts[val])
            if cnts[val] > 3:
                print(i, j, val, cnts[val])
                return
        i += 1


if __name__ == '__main__':
    find2()
