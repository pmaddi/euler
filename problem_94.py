'''
This is very slow but techincally works.

Could be improved by genreating pythagrean triples
'''


def square(x):
    return int(x ** .5) ** 2 == x


def opt1(s):
    right = (s // 2) ** 2
    l1 = (s + 1) ** 2
    if square(l1 - right):
        p = 2 * (s + 1) + s
        if p > 10 ** 9:
            return
        return p


def opt2(s):
    right = (s // 2) ** 2
    l2 = (s - 1) ** 2
    if square(l2 - right):
        p = 2 * (s - 1) + s
        if p > 10 ** 9:
            return
        return p


if __name__ == '__main__':
    sm = 0
    for s in range(3, 10 ** 9):
        if s % 2 == 1:
            continue
        right = (s // 2) ** 2
        o1 = opt1(s)
        if o1 is not None:
            sm += o1
        o2 = opt2(s)
        if o2 is not None:
            sm += o2
    print(sm)
