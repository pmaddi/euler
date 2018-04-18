import numpy as np
def make_divisor_sum(n):
    divisor_sum = np.zeros(n, dtype=int)
    for i in range(1, n + 1):
        for j in range(2, n // i + 1):
            if i * j <= n:
                v = divisor_sum[(i * j) - 1]
                divisor_sum[(i * j) - 1] = v + i
    return divisor_sum

def abundants_under(n):
    sm = make_divisor_sum(n)
    out = set()
    for idx, v in enumerate(sm):
        if v > idx + 1:
            out.add(idx + 1)
    return out

def pos_int_no_ab_sum_under(n):
    abundants = abundants_under(n)
    abundants_list = list(abundants)
    abundants_list.sort()
    out = set()
    for i in range(1, n):
        j_idx = 0
        val = abundants_list[j_idx]
        found = False
        while val < i:
            dif = i - val
            if dif in abundants:
                found = True
                break
            j_idx += 1
            val = abundants_list[j_idx]
        if not found:
            out.add(i)
    return out



if __name__ == '__main__':
    print(sum(pos_int_no_ab_sum_under(28123)))
