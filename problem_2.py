def s(t):
    cts = {0:1, 1:1}
    idx = 1
    evensum = 0
    while cts[idx] < t:
        if cts[idx] % 2 == 0:
            evensum += cts[idx]
        idx += 1
        cts[idx] = cts[idx - 1] + cts[idx - 2]
    return evensum

assert(s(1)==0)
assert(s(9)==10)
assert(s(35)==44)
print(s(4000000))
