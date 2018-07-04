from pathlib import Path
import json
#def in(lst, key):
#    for k in key:
#        lst.index(k)
#        if
# class Trie:
#     def __init__(self):
#         self.dct = {}
#
#     def add(self, key):
#         pass
#
# 123
# 1 34
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
    # dbls = set()
    # for t in trips:
    #     dbls.add(t[0:2])
    #     dbls.add(t[1:3])
    # print(dbls)
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

    # code = ''.join([str(a) for a in range(1,10)] * 20)#joined + joined
    code = joined + joined
    # for l in range(1000):
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

    # d = {}
    # for t in trips:
    #     tmp = d
    #     for c in t:
    #         dct = tmp.get(c, {})
    #         tmp[c] = dct
    #         tmp = dct
    # print(json.dumps(d, indent=4))
