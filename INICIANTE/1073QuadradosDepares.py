n = int(input())

i = 0

while i <= n:
    if i > 0 and i % 2 == 0:
        sqrt = i * i
        print(f"{i}^2 = {sqrt}")
    i += 1
