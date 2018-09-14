import math
ROMAN_TO_DIGITAL = {'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000}

def parse(st):
    single = ROMAN_TO_DIGITAL
    if st in single:
        return single[st]
    if single[st[0]] < single[st[1]]:
        mult = -1
    else:
        mult = 1
    return mult * parse(st[0]) + parse(st[1:])

def test_parse():
    ps = ['IIIIIIIIIIIIIIII',
          'VIIIIIIIIIII',
          'VVIIIIII',
          'XIIIIII',
          'VVVI',
          'XVI',]
    for p in ps:
        assert(parse(p) == 16)
    assert(parse('XIX') == 19)
    assert(parse('IX') == 9)
    assert(parse('XLIX') == 49)
    assert(parse('MDCVI') == 1606)

def generate(r):
    if r == 0:
        return ''
    pwr = int(math.log10(r)) + 1
    leading = r // (10 ** (pwr - 1))
    if pwr == 4:
        return 'M' + generate(r - 10 ** 3)
    elif pwr == 3:
        if leading == 9:
            return 'CM' + generate(r - 900)
        elif leading >= 5:
            return 'D' + generate(r - 500)
        elif leading == 4:
            return 'CD' + generate(r - 400)
        else:
            return 'C' + generate(r - 100)
    elif pwr == 2:
        if leading == 9:
            return 'XC' + generate(r - 90)
        elif leading >= 5:
            return 'L' + generate(r - 50)
        elif leading == 4:
            return 'XL' + generate(r - 40)
        else:
            return 'X' + generate(r - 10)
    elif pwr == 1:
        if leading == 9:
            return 'IX' + generate(r - 9)
        elif leading >= 5:
            return 'V' + generate(r - 5)
        elif leading == 4:
            return 'IV' + generate(r - 4)
        else:
            return 'I' + generate(r - 1)

def test_generate():
    assert(generate(10) == 'X')
    assert(generate(100) == 'C')
    assert(generate(9) == 'IX')
    assert(generate(19) == 'XIX')
    assert(generate(49) == 'XLIX')
    assert(generate(5000) == 'MMMMM')
    assert(generate(949) == 'CMXLIX')

if __name__ == '__main__':
    from pathlib import Path
    roms = Path('p089_roman.txt').read_text().split()
    orig_size = len(''.join(roms))
    new_size = len(''.join([generate(parse(r)) for r in roms]))
    print(orig_size - new_size)
