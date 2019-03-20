from numpy import rint
from numpy.polynomial.polynomial import Polynomial


def op(seq):
    if seq == [1]:
        return [1]
    return [
        int(i) for i in
        (
            rint(
                Polynomial
                .fit(range(1, len(seq) + 1), seq, len(seq) - 1)
                .convert()
                .coef[::-1]
            )
            .tolist()
        )
    ]


def test_op():
    assert op([1]) == [1]
    assert op([1, 8]) == [7, -6]
    assert op([1, 8, 27]) == [6, -11, 6]
    assert op([1, 8, 27, 64]) == [1, 0, 0, 0]


def ev(n, poly):
    exp = 0
    out = 0
    for v in poly[::-1]:
        out += v * (n ** exp)
        exp += 1
    return out


def test_ev():
    assert ev(1, [7, -6]) == 1
    assert ev(2, [7, -6]) == 8
    assert ev(3, [7, -6]) == 15


if __name__ == '__main__':
    pol = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1]
    vals = [ev(i, pol) for i in range(1, len(pol) + 1)]
    out = 0
    for j in range(1, len(pol)):
        fn = op(vals[:j])
        for idx, v in enumerate(vals):
            vPrime = ev(idx + 1, fn)
            if v != vPrime:
                out += vPrime
                break
    print(out)
