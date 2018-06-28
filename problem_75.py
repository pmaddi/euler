from math import gcd

N = 10000
N = 50
N = 1500000

if __name__ == '__main__':
    counts = {}
    for n in range(1, int(N ** .5) + 1):
        m = n + 1
        while True:
            if gcd(n, m) != 1:
                m += 1
                continue
            if not (m % 2 == 0 or n % 2 == 0):
                m += 1
                continue

            sm = 2 * m * n + 2 * (m ** 2)
            if sm > N:
                break

            k = 1
            while True:
                ksm = k *  sm
                if ksm > N:
                    break
                counts[ksm] = counts.get(ksm, 0) + 1
                k += 1
            m += 1
    print(sum(1 for i, j in counts.items() if j == 1))
