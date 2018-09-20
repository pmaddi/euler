'''
Slow... works tho
'''
def tri_valid(s1, s2, s3):
    s1, s2, s3 = sorted((s1, s2, s3))
    return (s1 ** 2 + s2 ** 2) == (s3 ** 2)

def almost_int(f):
    return int(f) == f

def valid(s1, s2, s3):
    shortest = min(
        ((s1 + s2) ** 2 + s3 ** 2),
        ((s1 + s3) ** 2 + s2 ** 2),
        ((s2 + s3) ** 2 + s1 ** 2))
    if almost_int(shortest ** .5):
        return True
    return False

def main():
    N = 1000000
    v_count = 0
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            for k in range(1, j + 1):
                if valid(i, j, k):
                    v_count += 1
        print(i, v_count)
        if v_count > 10**6:
            return

if __name__ == '__main__':
    main()
