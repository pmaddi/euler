def inc_rec(digits, maxdig):
    if digits == 1:
        return maxdig + 1
    if maxdig == 0:
        return 1
    return inc(digits - 1, maxdig) + inc(digits, maxdig - 1)


def inc(digits, maxdig):
    vals = [[1 for i in range(maxdig + 1)] for j in range(digits)]
    for r in range(digits):
        for c in range(maxdig + 1):
            digit = r + 1
            m = c
            if digit == 1:
                vals[r][c] = m + 1
                continue
            if m == 0:
                vals[r][c] = 1
                continue
            vals[r][c] = vals[r - 1][c] + vals[r][c - 1]
    return vals[-1][-1]


def test_inc():
    for incf in [inc, inc_rec]:
        assert incf(2, 1) == 3
        assert incf(2, 9) == 55
        assert incf(3, 9) == 220
        assert incf(4, 9) == 715


def dec_rec(digits, maxdig):
    if digits == 1:
        return maxdig + 1
    if maxdig == 0:
        return 1
    return dec(digits - 1, maxdig) + dec(digits, maxdig - 1) + (digits - 1)


def dec(digits, maxdig):
    vals = [[1 for i in range(maxdig + 1)] for j in range(digits)]
    for r in range(digits):
        for c in range(maxdig + 1):
            digit = r + 1
            m = c
            if digit == 1:
                vals[r][c] = m + 1
                continue
            if m == 0:
                vals[r][c] = 1
                continue
            vals[r][c] = vals[r - 1][c] + vals[r][c - 1] + (digit - 1)
    return vals[-1][-1]


def test_dec():
    for decf in [dec, dec_rec]:
        assert decf(2, 9) == 64
        assert decf(3, 9) == 283
        assert decf(4, 9) == 997


def non_bounce(digits):
    # Add the increasing and decreasing, and subtract out all the numebers that
    # are all repeats, as well as both counts of zeros.
    return inc(digits, 9) + dec(digits, 9) - (digits * 9 + 2)


def test_non_bounce():
    assert non_bounce(1) == 9
    assert non_bounce(2) == 99
    assert non_bounce(3) == 474
    assert non_bounce(6) == 12951
    assert non_bounce(10) == 277032


if __name__ == '__main__':
    print(non_bounce(100))
