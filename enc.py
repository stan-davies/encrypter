# Currently only works on lowercase text.

import re
import util

with open("plaintext", "r") as f:
        plain  = f.read()

plain += '\0'

symbols = "".join(filter(lambda x: (x >= 'a' and x <= 'z') or ' ' == x, plain)).split(' ')

reps = {}
for s in symbols:
        if s in reps:
                reps[s] += 1
        else:
                reps[s] = 1

# Might want to work out optimum rather than just picking a value.
filtered = [key for key in reps if reps[key] > 1]


with open("enc.bin", "wb") as f:
        for i in range(0, len(filtered)):
                plain = re.sub(f'{filtered[i]}', f'{chr(30)}{i}', plain)
                f.writelines([ord(c).to_bytes(1) for c in f'{i}{filtered[i]}\n'])
        f.writelines([ord(c).to_bytes(1) for c in plain])
