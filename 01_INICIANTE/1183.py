O = input().upper()

M = []

for i in range(12):
    line = []
    for j in range(12):
        E = float(input())
        line.append(E)
    M.append(line)

SUM = 0
count = 0

for i in range(12):
    for j in range(i + 1, 12):
        SUM += M[i][j]
        count += 1

if O == 'S':
    print(f"{SUM:.1f}")
elif O == 'M':
    average = SUM / count
    print(f"{average:.1f}")
