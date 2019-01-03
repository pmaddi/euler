'''
Works for 1,2 and not 3.
'''
from pathlib import Path

TEN_SET = set(range(1, 10))
class Board:
    def __init__(self, rows):
        self.rows = rows
        self.cols = tuple(zip(*self.rows))
        self.sections = tuple(
            tuple(set([]) for i in range(3)) for j in range(3))
        for di in range(3):
            for dj in range(3):
                for i in range(3):
                    for j in range(3):
                        self.sections[di][dj].add(
                            self.rows[di * 3 + i][dj * 3 + j])

    def replaced(self, i, j, val):
        l_rows = list(self.rows)
        l_col = list(l_rows[i])
        l_col[j] = val
        l_rows[i] = l_col
        return Board(tuple(tuple(j for j in i) for i in l_rows))

    def available(self, i, j):
        return (
            TEN_SET
            - set(self.rows[i])
            - set(self.cols[j])
            - self.sections[i // 3][j // 3]
            - set([0])
        )

    def filled(self):
        return not any((0 in i) for i in self.rows)

    def solved(self):
        for l in self.rows + self.cols:
            if not (set(l) - set([0])) == TEN_SET:
                return False
        for sr in self.sections:
            for l in sr:
                if not (l - set([0])) == TEN_SET:
                    return False
        return True

    def __str__(self):
        return '\n'.join(
            ' '.join(str(c) for c in r).replace('0', '_')
            for r in self.rows) + '\n'

    def next(self):
        '''Returns an iterable of boards'''
        locs = []
        for i in range(9):
            for j in range(9):
                if self.rows[i][j] == 0:
                    locs.append((i, j, self.available(i, j)))
        locs.sort(key=lambda x: len(x[2]))
        i, j, moves = locs[0]
        for m in moves:
            yield self.replaced(i, j, m)
        # for l in locs:
        #     i, j, moves = l
        #     for m in moves:
        #         print(self)
        #         yield self.replaced(i, j, m)

def btrack(opt):
    if opt.filled():
        if opt.solved():
            return opt
        else:
            return False
    cands = opt.next()
    for c in cands:
        resp = btrack(c)
        if resp:
            return resp


if __name__ == '__main__':
    lines = (
        Path('p096_sudoku.txt')
        .read_text()
        .split('\n')
    )
    sm = 0
    for i in range(len(lines) // 10):
        board = lines[((i * 10) + 1):((i + 1) * 10)]
        board = Board(tuple(tuple(int(i) for i in list(b)) for b in board))
        solution = btrack(board)
        r = solution.rows[0]
        sm += r[0] * 100 + r[1] * 10 + r[2]
    print(sm)
