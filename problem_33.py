if __name__ == '__main__':
    out = 1
    for i in range(10, 100):
        for j in range(i + 1, 100):
            si = str(i)
            sj = str(j)
            for s in si:
                if s != '0' and s in sj:
                    try:
                        n = int(si.replace(s, ''))
                        d = int(sj.replace(s, ''))
                        if d != 0 and j != 0 and i / j == n / d:
                            out *= (i / j)
                    except:
                        pass
    print(round(1 / out))
