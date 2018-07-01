import numpy as np
N = 100

def primes_lt(n):
    '''too slow'''
    nums = np.zeros(n - 1)
    nums[0] = 1
    for i in range(2, int(n ** .5) + 1):
        for j in range(2, (n // i) + 1):
            if i * j < n:
                nums[i * j - 1] = 1 # is nonprime
    primes = set()
    for i in range(len(nums)):
        if not nums[i]:
            primes.add(i + 1)
    return primes

def ways(vals):
    vals = sorted(list(set(vals)))
    lst = [0 for i in range(N)]
    lst[0] = 1
    for v in vals:
        for i in range(v, N):
            lst[i] += lst[i - v]
    return lst






    # tbl = np.ones((n, n + 1), dtype=int)
    # for idx_i in range(1, n):
    #     for idx_j in range(n + 1):
    #         other_val_idx = idx_j - (idx_i + 1)
    #         if other_val_idx >= 0:
    #             other = tbl[idx_i, other_val_idx]
    #         else:
    #             other = 0
    #         tbl[idx_i, idx_j] = tbl[idx_i - 1, idx_j] + other
    # return tbl[n-1, n] - 1

def get_min_idx_over(lst, val):
    for idx, v in enumerate(lst):
        if v > val:
            return idx

def main():
    print(get_min_idx_over(ways(primes_lt(N + 2)), 5000))

if __name__ == '__main__':
    # print(ways([1,2,3,4,5]))
    assert(ways([1,2,3,4,5])[5] == 7)
    assert(ways(primes_lt(N + 2))[10] == 5)
    assert(get_min_idx_over([1,3,5,7,10], 6) == 3)
    # print(ways(primes_lt(N + 2)))
    # print(ways(primes_lt(N + 2))[71])
    # print(ways(primes_lt(N + 2))[72])
    main()
