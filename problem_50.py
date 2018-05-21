import numpy as np
from itertools import combinations

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

if __name__ == '__main__':
    p_set = primes_lt(10 ** 6 + 1)
    p_lst = sorted(list(p_set))
    bsf = 0
    bsf_cnt = 1
    for i in range(len(p_lst)):
        for j in range(i + bsf_cnt, len(p_lst) + 1):
            sm = sum(p_lst[i: j])
            if sm > 10 ** 6:
                break
            if sm in p_set:
                if j - i > bsf_cnt:
                    bsf_cnt = j - i
                    bsf = sm
    print(bsf)

