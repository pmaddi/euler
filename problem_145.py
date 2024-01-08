if __name__ == '__main__':
    for i in range(10**3):
        j = int(''.join(reversed(str(i))))
        p = i + j
        # print(i)
        # print([int(v) for v in list(str(p))])
        # print([int(v) % 2 != 0 for v in list(str(p))])
        if all(int(v) % 2 != 0 for v in list(str(p))):
            print(p)
            print(i, j)
