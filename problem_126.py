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
    i, j, k = 1
    while(True):
        
    seen = []
    for i in range(1, 10):
        for j in range(i, 10):
            for k in range(j, 10):
                dims = [i, j, k]
                v = create(dims)
                seen.append((dims, len(gen_next(v)[1])))
    print(seen)

find()

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
