import math
def digits(x):
    return int(math.log10(x)) + 1

def lenof(x):
    if x < 10:
        return x
    d = digits(x)
    last_num_of_lower_thing = 10**(d - 1) - 1
    return (x - last_num_of_lower_thing) * d + lenof(last_num_of_lower_thing)

def bsearch(d):
    l = 0
    r = d
    while r - l > 1:
        med = (r-l) // 2 + l
        dec = lenof(med)
        # print('l', l, 'r', r, 'lenof(l)', lenof(l), 'lenof(r)', lenof(r), 'd', d, 'dec', dec, 'med', med)
        if dec < d:
            l = med
        elif dec > d:
            r = med
        else:
            return int(str(med)[-1])
    offset = d - lenof(l) - 1
    return int(str(r)[offset])

def do():
    m = 1
    for i in range(7):
        idx = 10**i
        m *= bsearch(idx)
    return m

if __name__ == '__main__':
    assert(lenof(11) == 13)
    assert(lenof(100) == 192)
    assert(lenof(99) == 189)

    assert(bsearch(1) == 1)
    assert(bsearch(10) == 1)

    assert(bsearch(11) == 0)
    assert(bsearch(12) == 1)

    print(do())
