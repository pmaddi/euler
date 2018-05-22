from math import factorial

def comb(n, k):
    return factorial(n) // factorial(k) // factorial(n - k)

def main():
    out = []
    for n in range(1, 101):
        for k in range(1, n + 1):
            c = comb(n, k)
            if c > 10**6:
                out.append(c)
    return len(out)

if __name__ == '__main__':
    print(main())

