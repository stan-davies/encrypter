# Currently only works on lowercase text.

import re
import util

with open("Aristotle", "r") as f:
        plain  = f.read()

plain += '\0'

symbols = ("".join(filter(lambda x: (x >= 'a' and x <= 'z') or ' ' == x, plain))).split(' ')

reps = {}
for s in symbols:
        if s in reps:
                reps[s] += 1
        else:
                reps[s.lower()] = 1


filtered = []
minr = 3
while True:
        for key in reps:
        # See README to see where numbers come from.
                if reps[key] >= minr and ( \
                   (len(key) >= 6 and reps[key] >= 2) \
                or (len(key) >= 4 and reps[key] >= 3) \
                or (len(key) == 3 and reps[key] >= 5)):
                        filtered.append(key)

        if len(filtered) <= 256:
                break

        minr += 1
        filtered = []
        print(f"{minr = } as {len(filtered) = }")

with open("enc.bin", "wb") as f:
        for i in range(0, len(filtered)):
                key = f'{chr(i)}'
                # Character with code 92 is '\' which confuses regex.
                if 92 == i:
                        key = '\\' + key
                plain = re.sub(f'{filtered[i]}', f'\x1e{key}', plain)
                f.writelines([ord(c).to_bytes(1) for c in f'{filtered[i]}\n'])
        f.write(b'\x1e\x1e\x1e')
        f.writelines([ord(c).to_bytes(1) for c in plain])
