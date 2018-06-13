from itertools import product

def flatten(x):
    for i in x:
        for j in i:
            yield j

def intjoin(x):
    return int(''.join(str(i) for i in x))

def make_set(nodes, sltn):
    outset = set(list(range(1, 2 * len(nodes) + 1)))
    if len(set(nodes)) != len(nodes):
        return None
    out = []
    vals = list(nodes)
    for i in range(len(nodes)):
        n1 = nodes[i]
        n2 = nodes[(i + 1) % len(nodes)]
        nxt = sltn - n1 - n2
        out.append((nxt, n1, n2))
        vals.append(nxt)
    if outset != set(vals):
        return None
    mi = min(enumerate(out), key=lambda x: x[1][0])[0]
    return out[mi:] + out[:mi]

def maxrng(node_count, numrange, solutionrange, digits):
    out = []
    for sltn in solutionrange:
        internals = [numrange for i in range(node_count)]
        for internal_nodes in product(*internals):
            m = make_set(internal_nodes, sltn)
            if m:
                s = intjoin(flatten(m))
                d = len(str(s))
                if d == digits:
                    out.append(s)
    return max(out)

def main():
    assert(maxrng(3, range(1, 7), range(9, 16), 9) == 432621513)
    print(maxrng(5, range(1, 11), range(9, 28), 16))

if __name__ == '__main__':
    main()
