import numpy as np
def build_arr_lt(n):
    arr = np.repeat(0, n - 1)
    arr[1 - 1] = 1 # 1 is considered composite
    for i in range(2, n // 2 - 1):
        if arr[i - 1] == 0: # if maybe prime
            max_mult = (n - 1) // i
            for multiples in range(2, max_mult + 1):
                arr[i * multiples - 1] = 1
    return arr
if __name__ == '__main__':
    arr = build_arr_lt(10 ** 6)
    import ipdb
    ipdb.set_trace()

