'''
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
        else:
            print(side1, side2, side3)

    side_max = 100# 3000
    rng = side_max // 2
    small_key_legs = {}
    large_key_legs = {}
    for n in range(1, rng):
        for m in range(n + 1, rng):
            k = 1
            while True:
                a = k * (m**2 - n**2)
                b = k*2*m*n
                # c = k * (m**2 + n**2)
                if min(a, b) > side_max:
                    break

                s, b = sorted((a, b))

                sv = small_key_legs.get(s, set())
                sv.add(b)
                small_key_legs[s] = sv
                lv = large_key_legs.get(b, set())
                lv.add(s)
                large_key_legs[b] = lv

                k += 1
            # if len(cache) == last:
            #     print(len(cache))
                # return
            # last = len(cache)
    print(small_key_legs)
    print(large_key_legs)
    for n in range(side_max):
        st = large_key_legs.get(n)
        if st:
            pass #



    # print(cache)

if __name__ == '__main__':
    main()
