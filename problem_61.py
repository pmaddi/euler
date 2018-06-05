import math

MAXVAL = 9999
MINVAL = 1000
STARTSET = {}

EQS = {
        '3':(lambda n: n*(n+1)//2 ),
        '4':(lambda n: n*n ),
        '5':(lambda n: n*(3*n-1)//2 ),
        '6':(lambda n: n*(2*n-1) ),
        '7':(lambda n: n*(5*n-3)//2 ),
        '8':(lambda n: n*(3*n-2) ),
        }

def digits(x):
    return int(math.log10(x)) + 1

def gen_under(sides):
    fn = EQS.get(str(sides))
    i = 1
    while True:
        v = fn(i)
        if v < MINVAL:
            i += 1
            continue
        if v > MAXVAL:
            return
        yield v
        i += 1

def bfs(root, node, to_see):
    val, num = node
    val_tail = val % 100
    head_of_root = root // 100

    if num not in to_see:
        return

    if len(to_see) == 1 and num in to_see and head_of_root == val_tail:
        return [node]

    new_to_see = to_see.copy() - {num}
    next_nodes = STARTSET.get(val_tail, [])
    for next_node in next_nodes:
        ret = bfs(root, next_node, new_to_see.copy())
        if ret:
            return [node] + ret

def start_bfs_from(node):
    return bfs(node[0], node, set(range(3, 9)))

def main():
    for i in range(3, 9):
        for j in gen_under(i):
            val = (j, i)
            start = j // 100
            tmp = STARTSET.get(start, set())
            tmp.add((j, i))
            STARTSET[start] = tmp

    for i in range(3, 9):
        for j in gen_under(i):
            val = (j, i)
            ret = start_bfs_from(val)
            if ret:
                return sum(i for i, j in ret)

if __name__ == '__main__':
    print(main())
