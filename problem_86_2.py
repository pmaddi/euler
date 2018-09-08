'''
generate side lengths (how many to generate?)
    break up both legs
        add a count to the right bucket
        dont store the cuboid sides because it should be unique? (is this true?)
            this kinda hinge on this capability :/

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

    def place(sides, origin):
        sides = tuple(sorted(sides))
        longest = max(sides)
        st = tbl.get(longest, {})
        if sides in st:
            print(sides, st[sides])
            raise ValueError('shouldve not seen dis')
        st[sides] = origin
        tbl[longest] = st

    side_max = 100# 3000
    rng = side_max // 2
    tbl = {}
    seen = set()
    for n in range(1, rng):
        for m in range(n + 1, rng):
            k = 1
            while True:
                a = k * (m ** 2 - n ** 2)
                b = k * 2 * m * n
                key = tuple(sorted((a, b)))
                if key not in seen:
                    seen.add(key)
                    # c = k * (m ** 2 + n ** 2)
                    print(a,b)
                    if min(a, b) > side_max:
                        break

                    for a1 in range(1, a // 2):
                        place((a1, a - a1, b), (a, b))

                    for b1 in range(1, b // 2):
                        place((b1, b - b1, a), (a, b))

                k += 1
    print(tbl)

if __name__ == '__main__':
    main()
