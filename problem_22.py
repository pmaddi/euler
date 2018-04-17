def cnt(st):
    nms = st.replace('"', '').split(',')
    nms.sort()
    out = 0
    for idx, name in enumerate(nms):
        name_sum = 0
        for c in name:
            name_sum += ord(c) - ord('A') + 1
        out += (idx + 1) * name_sum
    return out



if __name__ == '__main__':
    with open("p022_names.txt", 'r') as f:
        tx = f.read()
        print(cnt(tx))

