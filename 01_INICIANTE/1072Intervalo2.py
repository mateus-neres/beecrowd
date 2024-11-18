entrada = int(input())
i = 0
dentro = 0
fora = 0
while i < entrada:
    n = int(input())
    if n >= 10 and n <= 20:
        dentro += 1
    else:
        fora +=1
    i += 1
print(f"{dentro} in\n{fora} out")
