from math import factorial

def digits(n):
    return [int(i) for i in str(n)]

def dig_fact(n):
    return sum(factorial(x) for x in digits(n))

def explore(n, cache, seen):
    '''
    mutates cache
    returns chain length and loop values
    '''
    # print('explore', n, cache, seen)
    if n in cache:
        return cache[n], ()
    if n in seen:
        val = len(seen) - seen.index(n)
        inloop = seen[-val:]
        cache[n] = val
        return val, inloop
    nxt = dig_fact(n)
    if nxt == n:
        cache[n] = 1
        return 1, ()
    seen_new = seen + (n,)
    loop_depth, loopvals = explore(nxt, cache, seen_new)
    if n in loopvals:
        depth = loop_depth
    else:
        depth = loop_depth + 1
    cache[n] = depth
    return depth, loopvals

if __name__ == '__main__':
    assert(dig_fact(145) == 145)
    cache = {}
    count = 0
    for i in range(1, 10**6):
        d, _ = explore(i, cache, ())
        if d == 60:
            count += 1
    assert(cache[69] == 5)
    print(count)
