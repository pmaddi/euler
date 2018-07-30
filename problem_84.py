import pandas as pd
import random

COLS = 40
STATES = 40

GO = 0
C1 = 11
E3 = 24
H2 = 39
R1 = 5
G2J = 30

JAIL = 10
CC = [2, 17, 33]
CH = [7, 22, 36]
RAIL = [5, 15, 25, 35]
UTILITY = [12, 28]


def most_probable_str_series(stat):
    st = sorted(stat.items(), key=lambda x: x[1], reverse=True)
    out = ''
    for i, _ in st[:3]:
        out += str(i).zfill(2)
    return out

def roll_die(n):
    return random.sample(range(1, n + 1), 1)[0]

def all_doubles(lst: [(int, int)]) -> bool:
    if len(lst) != 3:
        return False
    for i, j in lst:
        if i != j:
            return False
    return True

def to_id(x):
    return x

def to_constant(loc):
    def closure(x):
        return loc
    return closure

def to_next_in(lst):
    def closure(x):
        for i in lst:
            if x < i:
                return i
        return lst[0]
    return closure

def to_back_3(x):
    return (x - 3) % STATES

def just_play(die):
    counts = {}
    last_3 = []
    state = 0
    for turn in range(10 ** 6):
        counts[state] = counts.get(state, 0) + 1
        die1, die2 = roll_die(die), roll_die(die)
        last_3 = (last_3 + [(die1, die2)])[-3:]

        if all_doubles(last_3):
            state = JAIL
            continue

        sm = die1 + die2
        state = (state + sm ) % STATES

        if state in CH:
            options = [to_id] * 6 + [
                    to_constant(GO),
                    to_constant(JAIL),
                    to_constant(C1),
                    to_constant(E3),
                    to_constant(H2),
                    to_constant(R1),
                    to_next_in(RAIL),
                    to_next_in(RAIL),
                    to_next_in(UTILITY),
                    to_back_3
                    ]
            fn = random.sample(options, 1)[0]
            state = fn(state)

        if state == G2J:
            state = JAIL

        if state in CC:
            options = [to_id] * 14 + [to_constant(GO), to_constant(JAIL)]
            fn = random.sample(options, 1)[0]
            state = fn(state)

    se = pd.Series(counts)
    return se / se.sum()


if __name__ == '__main__':
    assert(all_doubles([(1,1),(2,2),(3,3)]))
    assert(not all_doubles([(1,1),(2,2),(3,4)]))
    assert(most_probable_str_series(pd.Series({1: 3, 2: 1, 3: 0, 4: 9})) ==
            '040102')
    assert(most_probable_str_series(just_play(6)) == '102400')
    print(most_probable_str_series(just_play(4)))
