DIGS = 10
def powr(n):
    out = 1
    for i in range(n):
        out = (out * n) % (10 ** DIGS)
    return out

def addup(n):
    out = 0
    for i in range(1, n + 1):
        out = (out + powr(i)) % (10 ** DIGS)
    return out

if __name__ == '__main__':
    assert(addup(10) == 405071317)
    print(addup(1000) % (10 ** DIGS))



