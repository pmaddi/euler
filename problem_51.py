import numpy as np

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

def findall(st, sub):
    start = 0
    while True:
        idx = st.find(sub, start)
        if idx < 0:
            break
        yield idx
        start = idx + 1


def families(n):
    stn = str(n)
    outs = []
    for num in '1234567890':
        idxs = list(findall(stn, num))
        if len(idxs) < 1:
            continue
        for power in range(2 ** (len(idxs))):
            newstr = stn
            for j in range(len(idxs)):
                if (power >> j) & 1:
                    idx = idxs[j]
                    newstr = newstr[:idx] + '*' + newstr[idx + 1:]
            outs.append(newstr)
    return set(outs)

def main():
    primes = primes_lt(10**6)
    dt = {}
    for i in primes:
        for f in families(i):
            ls = dt.get(f, [])
            ls.append(i)
            dt[f] = ls
    msf_k = 0
    msf_v = 0
    msf_count = 0
    for i, j in dt.items():
        if len(j) > msf_count:
            msf_k = i
            msf_v = j
            msf_count = len(j)
    # print(msf_k, msf_v, msf_count)
    return min(msf_v)


if __name__ == '__main__':
    assert(list(findall('0560030', '0')) == [0, 3, 4, 6])
    print(main())
