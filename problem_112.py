from fractions import Fraction


def digits(n):
    out = []
    base = 1
    while base <= n:
        out.append(int((n / base) % 10))
        base *= 10
    return list(reversed(out))


def test_digits():
    assert digits(1) == [1]
    assert digits(101) == [1, 0, 1]
    assert digits(1234) == [1, 2, 3, 4]


def is_increasing(n):
    d = digits(n)
    if len(d) < 2:
        return True
    diffs = []
    prev = None
    for idx, val in enumerate(d):
        if idx != 0:
            diffs.append(val - prev)
        prev = val
    return min(diffs) >= 0


def is_decreasing(n):
    d = digits(n)
    if len(d) < 2:
        return True
    diffs = []
    prev = None
    for idx, val in enumerate(d):
        if idx != 0:
            diffs.append(val - prev)
        prev = val
    return max(diffs) <= 0


def is_bouncy(n):
    return not is_decreasing(n) and not is_increasing(n)


def test_is_bouncy():
    assert not is_bouncy(1)
    assert not is_bouncy(2)
    assert not is_bouncy(10)
    assert not is_bouncy(99)
    assert not is_bouncy(5)
    assert not is_bouncy(44)
    assert not is_bouncy(100)
    assert is_bouncy(101)
    assert is_bouncy(155349)


def find():
    n = 1
    bounces = 0
    while n < 10 or bounces / (n - 1) < 0.99:
        # if n > 10:
        #     print(bounces, n - 1, bounces / (n - 1))
        bounces += is_bouncy(n)
        n += 1
    print(bounces, n - 1, bounces / (n - 1))


if __name__ == '__main__':
    # Bouncy 2
    # Answer must be less than 2178000
    find()
    # cnt = 0
    # for i in range(1, 1000):
    #     cnt += is_bouncy(i)
    #     print(i, is_bouncy(i))
    # print(cnt)

    # print(proportion(21780))
    # print(float(proportion(2178000)))
    # print(proportion(21780) == Fraction(9, 10))
