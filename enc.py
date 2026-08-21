with open("plaintext", "r") as f:
        plain  = f.read()

plain += '\0'

reps = {}
sym = ""

symbols = "".join(filter(lambda x: (x >= 'a' and x <= 'z') or ' ' == x, plain.lower())).split(' ')

# Silly one liner for this?
for s in symbols:
        if s in reps:
                reps[s] += 1
        else:
                reps[s] = 1

# Might want to work out optimum rather than just picking a value.
filtered = [key for key in reps if reps[key] > 1]

print(f"{filtered = }")
