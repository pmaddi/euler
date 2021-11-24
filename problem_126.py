def create(d):
    l1 = set()
    for i in range(d[0]):
        for j in range(d[1]):
            for k in range(d[2]):
                l1.add((i, j, k))
    return l1


def gen_next(vol):
    """Returns total vol and last layer."""
    l2 = set()
    for i, j, k in vol:
        for delta in [-1, 1]:
            l2.add((i + delta, j, k))
            l2.add((i, j + delta, k))
            l2.add((i, j, k + delta))
    l2 = l2 - vol
    return vol | l2, l2 - vol


def find():
    counts = {}
    for i in range(1, 31):
        for j in range(1, i + 1):
            for k in range(1, j + 1):
                # print(i, j, k, i * j * k)
                dims = [i, j, k]
                v = create(dims)
                while True:
                    v, outer = gen_next(v)
                    sz = len(outer)
                    # print(sz)
                    counts[sz] = counts.get(sz, 0) + 1
                    if counts[sz] == 1000:
                        return sz
                    if sz > 1000:
                        break
    print(sorted(counts.items()))
    print(sorted(counts.items(), key=lambda x: x[1]))

if __name__ == '__main__':
    print(find())

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
