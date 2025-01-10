i = 0
while i <= 2:
    j = 1 + i
    for _ in range(3):
        if i == int(i):
            print(f"I={int(i)} J={int(j)}")
        else:
            print(f"I={i:.1f} J={j:.1f}")
        j += 1
    i = round(i + 0.2, 1)
