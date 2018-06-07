from math import sqrt

def rep(v):
    s = sqrt(v)
    initial = int(s)
    digits = [initial]
    seen = {}
    last_div = 1
    last_top_right = -1 * initial
    for idx in range(1, 10**5):
        h = (digits[idx - 1], last_div, last_top_right)
        sn = seen.get(h)
        if sn:
            return digits[(sn - 1):(idx - 1)]
        else:
            seen[h] = idx
        tmp_bottom = v - last_top_right ** 2
        assert(tmp_bottom / last_div == tmp_bottom // last_div)
        last_div = tmp_bottom // last_div
        if last_div == 0:
            return []
        val = int((s + -1 * last_top_right) / last_div)
        digits.append(val)
        last_top_right = -1 * last_top_right - last_div * val
    raise Exception('Couldnt find repeating for {}'.format(v))

if __name__ == '__main__':
    assert(sum([len(rep(i)) % 2 == 1 for i in range(2, 14)]) == 4)
    print(sum([len(rep(i)) % 2 == 1 for i in range(2, 10**4)]))
