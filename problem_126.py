"""
l3(n)=(2a+2c+4(n-1))*b +2*(generations outside)
genoutside = a*c + (2a+2c)*(n-1)+(n-2)*(n-1)/2*4

l3(n)=(2a+2c+4(n-1))*b +2*(a*c + (2a+2c)*(n-1)+(n-2)*(n-1)/2*4)
l3(n)=2ab+2cb+4nb-4b +2*(a*c + (2a+2c)*(n-1)+(n-2)*(n-1)*2)
l3(n)=2ab+2cb+4nb-4b + 2a*c + 4an - 4a + 4cn - 4c + 4n^2 - 12n + 8
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


if __name__ == '__main__':
    print(find_least(1000))

# v = create([1,2,3])
# l1 = v
# v, l2 = gen_next(v)
# v, l3 = gen_next(v)
# v, l4 = gen_next(v)
# v, l5 = gen_next(v)
# print(len(l1))
# print(len(l2))
# print(len(l3))
# print(len(l4))
# print(len(l5))
