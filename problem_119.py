def digsum(i):
    return sum(int(j) for j in str(i))

def find_opp():
    vals = []
    for base in range(2, 400):
        for exp in range(2, 9):
            pw = base ** exp
            ds = digsum(pw)
            if ds == base:
                vals.append((pw, base, exp))
    return sorted(vals)


if __name__ == '__main__':
    # for i, j in enumerate(find_opp()):
    #     print(i + 1, j)
    print(find_opp()[30 - 1][0])
