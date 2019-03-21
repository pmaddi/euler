from numpy import sqrt, arctan2, pi
from pathlib import Path
from pytest import approx


def c2p(x, y):
    return (sqrt(x**2 + y**2), arctan2(y, x))


def test_c2p():
    assert c2p(-1, 0) == (1, approx(pi))


def polar_dist(t1, t2):
    """The angle from t1 to t2.

    Note this always goes in the CCW direction."""
    if t2 > t1:
        return t2 - t1
    else:
        return 2 * pi - (t1 - t2)


def test_polar_dist():
    assert polar_dist(pi / 2, pi) == approx(pi / 2)
    assert polar_dist(pi, pi / 2) == approx(3 * pi / 2)


def contains(pts):
    polar = [c2p(x, y) for (x, y) in pts]
    c_pts = sorted(polar, key=lambda x: x[1])
    dsts = [
        polar_dist(c_pts[0][1], c_pts[1][1]),
        polar_dist(c_pts[1][1], c_pts[2][1]),
        polar_dist(c_pts[2][1], c_pts[0][1]),
    ]
    return max(dsts) <= pi


def test_contains():
    assert contains(((-340, 495), (-153, -910), (835, -947)))
    assert not contains(((-175, 41), (-421, -714), (574, -645)))


if __name__ == '__main__':
    lns = [
        [int(j) for j in i.split(',')]
        for i in
        Path('p102_triangles.txt').read_text().split()
    ]
    cnt = 0
    for p in lns:
        pts = [(p[0], p[1]), (p[2], p[3]), (p[4], p[5])]
        if contains(pts):
            cnt += 1
    print(cnt)
