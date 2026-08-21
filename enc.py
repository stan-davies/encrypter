import util


# So the encoded text will just have to be not really unicode. Probably have
# to write to the file as binary. Letters and numbers and so on will have the
# same identifiers, but then other stuff is being changed, so 30 will
# represent start of repitition block, and it expressly doesn't mean what it
# normally does.



plain = "well then loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooking 7 goooood aaaa keeeept"
pln_bt = [ord(c).to_bytes(1) for c in plain]
enc_bt = []

reps = 1 # every letter has one repitition of itself
prec = (0).to_bytes(1)
for c in pln_bt:
        if prec == c:
                reps += 1
        elif reps >= 4:         # Minimum for actually saving bytes in enc.
                del enc_bt[len(enc_bt) - reps:]
# Convert to '0xXX', minus 1 to give number of columns plus one, then divide,
# so 1,2 columns goes to 1 byte, 2,3 columns to 2B, 4,5 columns to 3B, ...
                width = (len(f"{hex(reps)}") - 1) // 2
                enc_bt.extend([util.ESC, reps.to_bytes(width), util.ESC, prec])
                reps = 1
        else:
                reps = 1

        enc_bt.append(c)
        prec = c

with open("enc.bin", "wb") as f:
        f.writelines(enc_bt)
