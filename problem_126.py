"""
l3(n)=(2a+2c+4(n-1))*b +2*(generations outside)
genoutside = a*c + (2a+2c)*(n-1)+(n-2)*(n-1)/2*4

l3(n)=(2a+2c+4(n-1))*b +2*(a*c + (2a+2c)*(n-1)+(n-2)*(n-1)/2*4)
l3(n)=2ab+2cb+4nb-4b +2*(a*c + (2a+2c)*(n-1)+(n-2)*(n-1)*2)
l3(n)=2ab+2cb+4nb-4b + 2a*c + 4an - 4a + 4cn - 4c + 4n^2 - 12n + 8

l3(n)=-4b - 4a- 4c  + 2ab+2cb+2ac+  4nb + 4an + 4cn + 4n^2 - 12n + 8
l3(n)=(-4 + 4n)(a + b + c)  + 2ab+2cb+2ac + 4n^2 - 12n + 8

l3(n)=-4*(a+b+c) + 4n(a+b+c)  + 2ab+2cb+2ac + 4n^2 - 12n + 8
l3(n)=4n^2 + n(4(a+b+c)-12)  + 2ab+2cb+2ac + 8 - 4*(a+b+c)
0=4n^2 + n(4(a+b+c)-12)  + 2ab+2cb+2ac + 8 - 4(a+b+c) - l3(n)

N = (-(4(a+b+c)-12) + sqrt((4(a+b+c)-12)^2 - 4*4*(2ab+2cb+2ac + 8 - 4(a+b+c) - l3(n)))) / (4*2)


2abc/c + 2cba/a + 2acb/b
2abc(1/a + 1/b + 1/c)

for each l3:
    for n in ???:
        find number of abc solutons?
"""


def layer_size(a, b, c, lr):
    gr = a * c
    if lr > 1:
        gr += (2 * a + 2 * c)*(lr - 1)
    if lr > 2:
        gr += (lr - 1) * (lr - 2) * 2
    gr *= 2
    gr += (2 * a + 2 * c + 4 * (lr - 1)) * b
    return gr


def test_layer_size():
    assert layer_size(1, 1, 1, 1) == 6
    assert layer_size(3, 2, 1, 1) == 22
    assert layer_size(3, 2, 1, 2) == 46
    assert layer_size(3, 2, 1, 3) == 78
    assert layer_size(3, 2, 1, 4) == 118


def find_least(cn):
    """
    This finds the solution but is quite slow. Apparently, my
    old solution + better constrained constrains on i, j , k
    gets you there much faster.
    """
    size = 13964
    lim_dim = 100000000
    msfv = 0
    msf = 0
    while True:
        cnt = 0
        for i in range(1, lim_dim):
            # import ipdb; ipdb.set_trace()
            if quadratic_valid(size, i, 1, 1) < 1:
                break
            for j in range(1, i + 1):
                if quadratic_valid(size, i, j, 1) < 1:
                    break
                for k in range(1, j + 1):
                    if quadratic_valid(size, i, j, k) < 1:
                        break
                    if is_valid(size, i, j, k):
                        cnt += 1
        if cnt == cn:
            return size
        if cnt > msf:
            msf = cnt
            msfv = size
        print(size, cnt, msfv, msf)
        size += 2


def find_least_1(cn):
    """
    dim 500, value 20k, got 16702
    dim 600, value 20k, got 18562
    15552
    not 19824
    not 19456
    not 20862
    not 22528
    not 30856
    not 18928
    not 19240
    not 19710
    not 15352

    weirdly, 2000, 17000 took 23 minutes and spat out 1761742

    """
    lim_dim = 2000
    lim_value = 17000
    counts = {}
    for i in range(1, lim_dim):
        for j in range(1, i + 1):
            for k in range(1, j + 1):
                lr = 0
                while True:
                    lr += 1
                    sz = layer_size(i, j, k, lr)
                    # if sz == 1792:
                    #     print(sz, i, j, k, lr)
                    counts[sz] = counts.get(sz, 0) + 1
                    if sz > lim_value:
                        break
    lsf = None
    for k, v in counts.items():
        if v != cn:
            continue
        print("candidate", k)
        if lsf is None or k < lsf:
            lsf = k
    return lsf


def sqrt(n):
    return n ** (.5)


def quadratic_valid(ll, a, b, c):
    sqval = ((4*(a+b+c)-12)**2 -
             4*4*(2*a*b+2*c*b+2*a*c + (8 - 4*(a+b+c) - ll)))
    if sqval < 0:
        return 0
    return (
        (-(4*(a+b+c)-12) +
         sqrt(sqval))
        / (4*2)
    )


def is_valid(ll, a, b, c):
    val = quadratic_valid(ll, a, b, c)
    rn = round(val)
    if abs(val - rn) < 0.00000001:
        if layer_size(a, b, c, rn) == ll:
            return True
    return False


if __name__ == '__main__':
    print(find_least(1000))
