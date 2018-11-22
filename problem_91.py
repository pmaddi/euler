def slope(p, q):
    '''returns None if div by zero
    '''
    d = q[0] - p[0]
    if d == 0:
        return
    else:
        return (q[1] - p[1]) / d

def two_slopes_prependicular(m1, m2):
    if m1 is None and m2 == 0:
        return True
    if m1 == 0 and m2 is None:
        return True
    if m1 is None or m2 is None:
        return False
    return m1 * m2 == -1


def forms_right_triangle(p, q):
    '''If the triangle formed by the origin, p, and q contains a right angle
    '''
    origin = (0, 0)
    s1 = slope(origin, p)
    s2 = slope(origin, q)
    m = slope(p, q)
    return (two_slopes_prependicular(s1, m) or
            two_slopes_prependicular(s2, m) or
            two_slopes_prependicular(s1, s2))

def points(n):
    for i in range(n + 1):
        for j in range(n + 1):
            if (i, j) != (0, 0):
                yield (i, j)

def count(n):
    cnt = 0
    for p in points(n):
        for q in points(n):
            if p != q and forms_right_triangle(p, q):
                cnt += 1
    return cnt // 2

def test_slope():
    assert slope((0, 0), (0, 1)) is None
    assert slope((0, 0), (1, 1)) == 1
    assert slope((1, 5), (5, 3)) == -0.5

def test_two_slopes_prependicular():
    assert two_slopes_prependicular(None, 0)
    assert two_slopes_prependicular(0, None)
    assert two_slopes_prependicular(-1/2, 2)
    assert two_slopes_prependicular(1, -1)
    assert not two_slopes_prependicular(1/2, 2)
    assert not two_slopes_prependicular(-1/2, -2)

def test_forms_right_triangle():
    assert forms_right_triangle((1, 0), (0, 1))
    assert forms_right_triangle((1, 1), (0, 2))
    assert forms_right_triangle((0, 3), (1, 3))
    assert forms_right_triangle((1, 3), (0, 3))
    assert not forms_right_triangle((2, 4), (0, 3))
    assert not forms_right_triangle((4, 4), (5, 5))

def test_count():
    assert count(1) == 3
    assert count(2) == 14

if __name__ == '__main__':
    print(count(50))
