if __name__ == '__main__':
    def r(n):
        return ''.join(reversed(n))

    out = 0
    for i in range(1, 10**6):
        d = str(i)
        b = bin(i)[2:]
        if r(d) == d and r(b) == b:
            out += i
    print(out)
