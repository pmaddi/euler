from pathlib import Path

def make_exp(base, exp):
    return base ** exp

def argmax(lst):
    msf = None
    msf_idx = 0
    for idx, i in enumerate(lst):
        if msf is None or i > msf:
            msf = i
            msf_idx = idx
        print('>>>', idx, msf_idx)
    return msf_idx

if __name__ == '__main__':
    r  = Path('p099_base_exp.txt').read_text()
    s = r.split()[:100]
    q = [[int(j) for j in i.split(',')] for i in s]
    q1 = (make_exp(*i) for i in q)
    print(argmax(q1) + 1)
