'''
Takes 9 minutes while the c version takes 9 seconds!!!!!
'''
def main():
    s = 0
    i = 1
    x = 0
    j = 0
    k = 0
    while True:
        for j in range(1, i + 1):
            for k in range(1, j + 1):
                x = (i * i)+(k + j)*(k + j);
                sq = x ** .5
                if int(sq) == (sq):
                    s += 1
                if s > 10 ** 6:
                    print(i)
                    return
        i += 1
if __name__ == '__main__':
    main()
