'''
next is n/2 if even
next is 3n+1 if odd
'''
def next(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def max_collatz_chain(under):
    chain_length = {1: 0}
    maxlen_n = 0
    maxlen = 0
    for n in range(1, under + 1):
        seq = []
        nxt = n
        while chain_length.get(nxt) is None and nxt != 1:
            seq.append(nxt)
            nxt = next(nxt)
        offset = chain_length.get(nxt, 0)
        for i, j in enumerate(seq):
            chain_length[j] = len(seq) + offset - i
        if len(seq) + offset > maxlen:
            maxlen = max(len(seq) + offset, maxlen)
            maxlen_n = n
    return maxlen_n

print(max_collatz_chain(1000000))
