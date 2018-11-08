from pathlib import Path
from math import log

def argmax(lst):
    msf = None
    msf_idx = 0
    for idx, i in enumerate(lst):
        if msf is None or cmp(i, msf) == -1:
            msf = i
            msf_idx = idx
    return msf_idx

def cmp(n1, n2):
    b1, e1 = n1
    b2, e2 = n2
    st = (e1 * log(b1)) / (e2 * log(b2))
    if st == 1:
        return 0
    elif st < 1:
        return 1
    else:
        return -1

def test_cmp():
    assert cmp((2, 11), (3, 7)) == 1
    assert cmp((632382, 518061), (519432, 525806)) == -1
    assert cmp((519432, 525806), (632382, 518061)) == 1

if __name__ == '__main__':
    r  = Path('p099_base_exp.txt').read_text()
    s = r.split()
    q = ([int(j) for j in i.split(',')] for i in s)
    print(argmax(q) + 1)
