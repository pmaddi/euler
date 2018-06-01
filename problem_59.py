from pathlib import Path

def xor(key, code):
    '''
    key: string
    code: int
    returns the decrypted string
    '''
    return ((int.from_bytes(key.encode('ascii') , 'big')
             ^ code)
            .to_bytes(1, 'big')
            .decode('ascii'))

def big_xor(key, body):
    out = 0
    msg = ''
    for i in range(len(body)):
        c = (xor(key[i % len(key)], body[i]))
        if not ord(c) in range(32, 127):
            return None, None
        out += ord(c)
        msg += c#.decode('ascii')
    if ' a ' not in msg:
        return None, None
    if ' in ' not in msg:
        return None, None
    return out, msg
if __name__ == '__main__':
    TXT = Path('p059_cipher.txt').read_text()
    BODY = [int(i) for i in TXT.split(',')]
    rn = range(ord('a'), ord('{'))
    for i in rn:
        for j in rn:
            for k in rn:
                key = chr(i) + chr(j) + chr(k)
                val, msg = big_xor(key, BODY)
                if val is not None:
                    print(val)
