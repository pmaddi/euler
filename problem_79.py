'''
Basically by hand
'''
from pathlib import Path
from collections import Counter

def is_in(lst, key):
    if not lst and key:
        return False
    elif not key:
        return True
    fst = key[0]
    try:
        idx = lst.index(fst)
    except ValueError:
        idx = None
    if idx is not None:
        return is_in(lst[idx:], key[1:])

def valid(lst, keys):
    return all(is_in(lst, k) for k in keys)


if __name__ == '__main__':
    nums = Path('p079_keylog.txt').read_text().split()
    trips = sorted(list(set(nums)))
    assert(is_in('12345', '234'))
    assert(is_in('12345', ''))
    assert(is_in('12345432', '242'))
    assert(not is_in('12345432', '251'))
    joined = ''.join(trips)
    assert(is_in(joined, trips[0]))
    assert(valid(joined, trips))
    assert(valid(joined + joined, trips))

    code = joined + joined
    code = '731628980'
    assert(valid(code, trips))
    while True:
        dropcount = 0
        for idx, _ in enumerate(code[::-1]):
            new_code = code[:idx] + code[idx+1:]
            if valid(new_code, trips):
                code = new_code
                dropcount += 1
        if dropcount == 0:
            break
        # if not l % 100:
        #     code = code + code
    print(code)
    # 73162890
