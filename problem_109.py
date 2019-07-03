if __name__ == '__main__':
    opts = []
    for n in range(1, 21):
        opts += [n, n * 2, n * 3]
    opts += [0, 25, 50]
    opts_unique = sorted(opts)
    two_shot = [0] * 171
    for i in range(len(opts_unique)):
        for j in range(i, len(opts_unique)):
            val = opts_unique[i] + opts_unique[j]
            two_shot[val] += 1
    three_shot = [0] * 171
    for target in range(171):
        count = 0
        rng = list(range(1, 21))
        rng.append(25)
        for n in rng:
            way_id = target - (n * 2)
            if way_id >= 0:
                count += two_shot[way_id]
        three_shot[target] = count
    assert three_shot[6] == 11
    assert three_shot[170] == 1
    print(sum(three_shot[:100]))
