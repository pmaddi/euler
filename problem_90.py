'''
Go thru all dicings

Oops! Didn't notice values on the cubes needn't be unique.
'''
PR = (
        (0, 1),
        (0, 4),
        (0, 9),
        (1, 6),
        (2, 5),
        (3, 6),
        (4, 9),
        (6, 4),
        (8, 1)
)


def expects(d):
    if d == 6 or d == 9:
        return [6, 9]
    return [d]


def makes_pair_h(pr, i, j):
    if not any(((v in expects(pr[0])) for v in i)):
        return False
    if not any(((v in expects(pr[1])) for v in j)):
        return False
    return True


def makes_pair(pr, i, j):
    return makes_pair_h(pr, i, j) or makes_pair_h(pr, j, i)


def valid(i, j):
    return all((makes_pair(p, i, j) for p in PR))


def test_valid():
    assert valid((0, 5, 6, 7, 8, 9), (1, 2, 3, 4, 8, 9))
    assert valid((0, 5, 1, 7, 8, 9), (1, 2, 3, 4, 8, 9))
    assert not valid((0, 0, 0, 0, 0, 0), (1, 2, 3, 4, 8, 9))


if __name__ == '__main__':
    lst = set()
    for i in range(2 ** 10):
        v = bin(i)[2:].zfill(10)
        st = []
        for c, x in enumerate(v):
            if x == '1':
                st.append(c)
        if len(st) == 6:
            lst.add(tuple(st))
    lst_two = set()
    for i in lst:
        for j in lst:
            lst_two.add(tuple(sorted((i, j))))
    cnt = 0
    for i in lst:
        for j in lst:
            print(i, j, valid(i, j))
            if valid(i, j):
                cnt += 1
    print(cnt)
