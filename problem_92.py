CACHE = {}
CACHE_SQ = {}

def square_digit_sum(i):
    if i in CACHE_SQ:
        return CACHE_SQ[i]
    out = 0
    for j in str(i):
        out += int(j) ** 2
    CACHE_SQ[i] = out
    return out


def arrives_at_89(i):
    if i in CACHE:
        return CACHE[i]
    next_value = square_digit_sum(i)
    if next_value == 1:
        CACHE[i] = False
        return False
    elif next_value == 89:
        CACHE[i] = True
        return True
    else:
        val = arrives_at_89(next_value)
        CACHE[i] = val
        return val

def test_square_digit_sum():
    assert square_digit_sum(1) == 1
    assert square_digit_sum(58) == 89
    assert square_digit_sum(10) == 1
    assert square_digit_sum(145) == 42

def test_arrives_at_89():
    assert arrives_at_89(1) == False
    assert arrives_at_89(44) == False
    assert arrives_at_89(13) == False
    assert arrives_at_89(85) == True
    assert arrives_at_89(145) == True
    assert arrives_at_89(89) == True


if __name__ == '__main__':
    cnt = 0
    for i in range(1, 10 ** 7):
        if arrives_at_89(i):
            cnt += 1
    print(cnt)
