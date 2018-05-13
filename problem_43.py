from itertools import permutations
def correct(x):
    return (
            int(x[1:4] ) % 2  == 0 and
            int(x[2:5] ) % 3  == 0 and
            int(x[3:6] ) % 5  == 0 and
            int(x[4:7] ) % 7  == 0 and
            int(x[5:8] ) % 11 == 0 and
            int(x[6:9] ) % 13 == 0 and
            int(x[7:10]) % 17 == 0
            )

def do():
    out = set()
    for i in permutations(range(10)):
        st = ''.join((str(j) for j in i))
        if correct(st):
            out.add(int(st))
    return sum(out)

if __name__ == '__main__':
    assert(correct('1406357289'))
    assert(not correct('1406357284'))
    print(do())

