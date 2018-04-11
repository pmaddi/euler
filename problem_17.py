import math
def produce(num, cache):
    if num in cache:
        return cache[num]
    length = int(math.log10(num)) + 1
    if length == 2:
        ones = num % 10
        tens = num - ones
        val = cache[tens] + '-' + cache[ones]
        cache[num] = val
        return val

    elif length == 3:
        hundreds = ((num // (10 ** 2)) % 10)
        rest_num = num - (hundreds * 100)
        rest = ''
        if rest_num:
            rest = ' and ' + cache[rest_num]
        val = cache[hundreds] + ' hundred' + rest
        cache[num] = val
        return val
    else:
        assert(False)

def num_letter_counts(n):
    cache = {
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine',
            10: 'ten',
            11: 'eleven',
            12: 'twelve',
            13: 'thirteen',
            14: 'fourteen',
            15: 'fifteen',
            16: 'sixteen',
            17: 'seventeen',
            18: 'eighteen',
            19: 'nineteen',
            20: 'twenty',
            30: 'thirty',
            40: 'forty',
            50: 'fifty',
            60: 'sixty',
            70: 'seventy',
            80: 'eighty',
            90: 'ninety',
            100: 'one hundred',
            1000: 'one thousand'
            }
    ct = ''
    for i in range(1, n + 1):
        st = produce(i, cache)
        st = st.replace(' ', '').replace('-', '')
        ct += st
    return len(ct)

def test_num_letter_counts():
    assert(num_letter_counts(5) == 19)

if __name__ == '__main__':
    test_num_letter_counts()
    print(num_letter_counts(1000))
