with open("enc.bin", "rb") as f:
        enc = f.read()

plain = ""
esc = False
reps = 1
beg = 0

for i in range(0, len(enc)):
        if 30 == enc[i]:
                if esc:
# Not really needed at all because reps is stored as an actual number so takes
# up a single byte but you can never be too careful.
                        slc = "".join([f"{s}" for s in enc[beg + 1:i]])
                        reps = int(slc) # What if fails??
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
