from problem_8 import assertEqual

import logging

import numpy as np

arr = np.repeat(0, 2000000)

def build_arr_lt(n):
    arr = np.repeat(0, n - 1)
    arr[1 - 1] = 1 # 1 is considered nonprime
    for i in range(2, n):
        max_mult = (n - 1) // i
        for multiples in range(2, max_mult + 1):
            arr[i * multiples - 1] = 1
    return arr

def sum_arr_primes(arr):
    max_val = len(arr)
    r_sum = 0
    for i in range(max_val):
        if arr[i - 1] == 0:
            r_sum += i
    return r_sum

def test_build_arr_until():
    assert(all(np.array([1, 0, 0, 1, 0, 1, 0, 1, 1]) == build_arr_lt(10)))

def test_sum_arr_primes():
    assertEqual(sum_arr_primes(np.array([1, 0, 0, 1, 0, 1, 0, 1, 1, 1])), 17)
    assertEqual(sum_arr_primes(np.array([1, 0, 0, 1, 0, 1, 0, 1, 1])), 17)

if __name__ == '__main__':
    test_build_arr_until()
    test_sum_arr_primes()
    print(sum_arr_primes(build_arr_lt(2000000)))
