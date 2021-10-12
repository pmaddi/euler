if __name__ == '__main__':
    paths = [(1,)]
    path_lengths = {}
    for p in paths:
        last_val = p[-1]
        prev_path_length = path_lengths.get(last_val)
        new_path_length = len(p) - 1
        if new_path_length > 200:
            continue
        if prev_path_length:
            path_lengths[last_val] = min(new_path_length, prev_path_length)
        else:
            path_lengths[last_val] = new_path_length
        for adder in reversed(p):
            paths.append(tuple(sorted(list(p + (last_val + adder,)))))
        if all(i in path_lengths for i in range(1, 201)):
            print(sum(path_lengths[i] for i in range(1, 201)))
            break
