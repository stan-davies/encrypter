# So the encoded text will just have to be not really unicode. Probably have
# to write to the file as binary. Letters and numbers and so on will have the
# same identifiers, but then other stuff is being changed, so 30 will
# represent start of repitition block, and it expressly doesn't mean what it
# normally does.



plain = "loooooooooooooooooooooking 7 goooood aaaa keeeept"
enc = []

reps = 1 # every letter has one repitition of itself
prec = ''
for c in plain:
        if prec == c:
                reps += 1
        elif reps > 1:
                del enc[len(enc) - reps:]
                enc.extend([30, reps, 30, ord(prec)])
                reps = 1

        enc.append(ord(c))
        prec = c

with open("enc.bin", "wb") as f:
        f.writelines([c.to_bytes(1) for c in enc])
