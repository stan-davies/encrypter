with open("enc.bin", "rb") as f:
        enc = f.read()

plain = ""
cnt = False
reps = 1

for d in enc:
        if 30 == d:
                cnt = not cnt
        elif cnt:
                reps = d
        elif reps > 1:
                plain += chr(d) * reps
                reps = 1
        else:
                plain += chr(d)


print(f"got '{plain}'")
