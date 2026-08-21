import util
import re

with open("enc.bin", "rb") as f:
        [dictionary, enc] = (''.join([chr(b) for b in f.read()])).split('\x1e\x1e')

subs = re.findall(r'.(\w+)\n', dictionary)

plain = ''
esc = False

for c in enc:
        if '\x1e' == c:
                esc = True
        elif esc:
                plain += subs[ord(c)]
                esc = False
        else:
                plain += c

with open('dec', 'w') as f:
        f.write(plain)
