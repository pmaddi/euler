def st(it):
    return tuple(sorted(str(it)))


def main():
    i = 1
    while True:
        vals = [st(i * m) for m in range(1, 7)]
        if len(set(vals)) == 1:
            return i
        i += 1

if __name__ == '__main__':
    assert(st(125874) == st(251748))
    print(main())
