if __name__ == '__main__':
    # 28433 * 2 ** 7830457 + 1
    n = 28433
    for i in range(7830457):
        n = n * 2 % (10 ** 10)
    print(n + 1)
