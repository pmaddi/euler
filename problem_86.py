'''
ugh idk
still no idea
'''
def isin(v):
    return v > 0 and v <= N

def tri_valid(s1, s2, s3):
    s1, s2, s3 = sorted((s1, s2, s3))
    return (s1 ** 2 + s2 ** 2) == (s3 ** 2)

def valid(s1, s2, s3):
    return all([isin(s) for s in [s1, s2, s3]])

def place(side1, side2, side3):
    if valid(side1, side2, side3):
        cache.add(tuple(sorted((side1, side2, side3))))

if __name__ == '__main__':
    N = 100
    sqn = 30
    cache = set()
    for i in range(1, sqn):
        for j in range(i + 1, sqn):
            m = j**2 + i**2
            n = j**2 - i**2
            k = int((m**2-n**2)**.5)

            short_l, long_l, hyp = sorted((m, n, k))
            if not tri_valid(short_l, long_l, hyp):
                print(m, n, k)
                continue

            for side2 in range(1, long_l):
                side1 = short_l
                side3 = long_l - side2
                place(side1, side2, side3)

            for side2 in range(1, short_l):
                side1 = long_l
                side3 = short_l - side2
                place(side1, side2, side3)
    print(cache)
    print(len(cache))
