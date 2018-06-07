from math import sqrt#, log10

def hsh(f, a):
    return '{}, {}'.format(str(f)[:6], a[-3:])
    # return '{}, {}'.format(str(f)[:6], 1)

def rep(v):
    s = sqrt(v)
    initial = int(s)# % 10
    digits = [initial]
    st = s - initial
    seen = {}
    for idx in range(1, 10**5):
        h = hsh(st + digits[-1], digits)
        sn = seen.get(h)
        if sn:
            # print(digits)
            # print(seen)
            return digits[(sn - 1):(idx - 1)]
        else:
            seen[h] = idx
        if st == 0:
            return []
        nxt = int(1 / st)
        digits.append(nxt)
        st = 1 / st - nxt
    print(digits)
    print(seen)
    raise Exception('Couldnt find repeating for {}'.format(v))
    # print("None. {}".format(v))

# print(sum([len(rep(i)) % 2 == 1 for i in range(2, 10**4)]))
# print(rep(83))
# print(rep(76))
# for i in range(70, 90):
#     print(i, len(rep(i)))

assert(sum([len(rep(i)) % 2 == 1 for i in range(2, 14)]) == 4)



print(sum([len(rep(i)) % 2 == 1 for i in range(2, 10**4)]))

# print(rep(285))
