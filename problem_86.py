'''
Correct, too slow

Sad.
'''

def main():
    def isin(v):
        return v > 0 and v <= side_max

    def tri_valid(s1, s2, s3):
        s1, s2, s3 = sorted((s1, s2, s3))
        return (s1 ** 2 + s2 ** 2) == (s3 ** 2)

    def almost_int(f):
        return int(f) == f

    def valid(s1, s2, s3):
        if not all([isin(s) for s in [s1, s2, s3]]):
            return False
        shortest = min(
            ((s1 + s2) ** 2 + s3 ** 2),
            ((s1 + s3) ** 2 + s2 ** 2),
            ((s2 + s3) ** 2 + s1 ** 2))
        if almost_int(shortest ** .5):
            return True
        return False

    def place(side1, side2, side3):
        if valid(side1, side2, side3):
            cache.add(tuple(sorted((side1, side2, side3))))
    side_max = 99# 3000
    rng = side_max // 2
    cache = set()
    last = 0
    for n in range(1, rng):
        for m in range(n + 1, rng):
            k = 1
            while True:
                a = k * (m**2 - n**2)
                b = k*2*m*n
                # c = k * (m**2 + n**2)
                if min(a, b) > side_max :
                    break

                for a1 in range(1, a):
                    place(a1, a - a1, b)

                for b1 in range(1, b):
                    place(b1, b - b1, a)

                k += 1
            # if len(cache) == last:
            #     print(len(cache))
                # return
            # last = len(cache)
    # print(cache)
    print(len(cache))

if __name__ == '__main__':
    main()
