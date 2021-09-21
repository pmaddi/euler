from math import floor


def arr(n, k):
    out = []
    for i in range(k):
        out.append([0] * n)
    return out


def build(n):
    pdf = arr(n + 1, n)
    for i in range(n):
        for j in range(i + 2):
            ad = 0
            if i - 1 >= 0:
                ad += pdf[i - 1][j] * (float(i + 1) / float(i + 2))
            if j - 1 >= 0:
                ad += pdf[i - 1][j - 1] * (1.0 / float(i + 2))
            if i == 0:
                ad = 1.0 / 2
            pdf[i][j] = ad
    return floor(1 / sum(pdf[-1][n // 2 + 1:]))


def test_build():
    assert build(4) == 10


# EV < 1
# ev = P(win) * payout
# 1 > P(win) * payout
# 1 / P(win) > payout

if __name__ == '__main__':
    print(build(15))
