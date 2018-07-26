import numpy as np
import pandas as pd

COLS = 40

def dice_odds(size):
    se = pd.Series([])
    for i in range(size):
        for j in range(size):
            v = i + j + 2
            se[v] = se.get(v, 0) + 1
    return se / se.sum()

def test_dice_odds():
    assert(dice_odds(6)[2] == 1/36)
    assert(dice_odds(6)[12] == 1/36)

def just_dice_matrix(dice_size):
    mat = np.zeros(shape=(COLS, COLS))
    mat = np.mat(mat)
    odds = dice_odds(dice_size)
    for i in range(COLS):
        for offset, prob in odds.iteritems():
            mat[i, (i + offset) % COLS] = prob
    return mat

def stationary(mat):
    powr = mat
    for i in range(1000):
        powr = powr * mat
    return np.array(powr)[0]

def most_probable_str(stat):
    st = sorted(list(enumerate(stat)), key=lambda x: x[0], reverse=True)
    out = ''
    for i, _ in st[:3]:
        out += str(i).zfill(2)
    return out

def p_84(sides):
    mat = just_dice_matrix(6)
    stab = stationary(mat)
    return most_probable_str(stab)


if __name__ == '__main__':
    test_dice_odds()
    # assert(p_84(6) == '102400')
    # print(p_84(4))
