def atoi(c):
    return ord(c) - ord('A') + 1

def wordsum(st):
    return sum([atoi(i) for i in st])

def mktriangles(n):
    out = set()
    for i in range(1, n):
        out.add(i * (i - 1) // 2)
    return out

def do():
    tr = mktriangles(1000)
    with open('p042_words.txt', 'r') as fl:
        ot = fl.read()
        l = ot.split(',')
        l = [wordsum(i.strip('"')) for i in l]
        j = [i for i in l if i in tr]
        print(len(j))

if __name__ == '__main__':
    assert(atoi('A') == 1)
    assert(atoi('Z') == 26)
    assert(wordsum('SKY') == 55)
    do()
