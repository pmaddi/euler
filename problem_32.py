if __name__ == '__main__':
    out = set()
    for i in range(1, 100):
        for j in range(10, 10000):
            ij = i * j
            st = ''.join(sorted(str(ij) + str(i) + str(j)))
            if st == '123456789':
                out.add(ij)
    print(sum(out))

