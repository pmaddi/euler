'''
p(n) = n(3n - 1)/2
p(n) = 3/2 n^2 - 1/2 n
0 = 3/2 n^2 - 1/2 n - p(n)

(1/2 +- squrt(1/4 - 4(3/2)(- pn))) / 3
'''
MAX = 10 ** 4
def is_int(n):
    return int(n) == n

def smdf(j, k):
    return (pent(j) + pent(k), abs(pent(k) - pent(j)))

def inverses(j, k):
    return (real_inverse_pent(pent(j) + pent(k)), real_inverse_pent(abs(pent(k) - pent(j))))

def find():
    min_d = 10**10
    for k in range(2, MAX + 1):
        for j in range(1, k):
            sm = pent(j) + pent(k)
            df = abs(pent(k) - pent(j))
            # print(j, k, sm, df, real_inverse_pent(sm), real_inverse_pent(df))
            if is_int(real_inverse_pent(sm)) and is_int(real_inverse_pent(df)):
            # if is_int(real_inverse_pent(df)):
               min_d = min(df, min_d)
               print(min_d)

def squrt(x):
    return x**(1/2)

def inverse_pent(p_n):
    return ((1/2 + squrt(1/4 - 4 * (3/2) * (-1 * p_n))) / 3,
            (1/2 - squrt(1/4 - 4 * (3/2) * (-1 * p_n))) / 3)

def real_inverse_pent(p_n):
    return inverse_pent(p_n)[0]

def pent(n):
    return n * (3*n - 1) / 2

def pent2(n):
    return 3/2 * n ** 2 - 1/2 * n

if __name__ == '__main__':
    find()
