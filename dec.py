import util

with open("enc.bin", "rb") as f:
        enc = f.read()

plain = ""
esc = False
reps = 1
beg = 0

for i in range(0, len(enc)):
        if util.ESC == enc[i]:
                if esc:
                        reps = int.from_bytes(enc[beg + 1:i])
                else:
                        beg = i
                esc = not esc
                continue

        if esc:
                continue

        if reps > 1:
                plain += chr(enc[i]) * reps
                reps = 1
        else:
                plain += chr(enc[i])

if esc:
        print("Unclosed escape sequence. You know how I feel about that sort of thing =(")


print(f"got '{plain}'")
