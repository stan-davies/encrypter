# Currently only works on lowercase text.

import re
import util

with open("big_sample", "r") as f:
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
filtered = [key for key in reps if reps[key] > 5 and len(key) > 2]


with open("enc.bin", "wb") as f:
        for i in range(0, len(filtered)):
                plain = re.sub(f'{filtered[i]}', f'\x1e{chr(i)}', plain)
                f.writelines([ord(c).to_bytes(1) for c in f'{chr(i)}{filtered[i]}\n'])
        f.write(b'\x1e\x1e')
        f.writelines([ord(c).to_bytes(1) for c in plain])
