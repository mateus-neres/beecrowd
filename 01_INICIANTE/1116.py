n = int(input())

for i in range(n):
    x, y = map(float, input().split())
    if y == 0 and x != 0:
        print("divisao impossivel")
    else:
        div = x / y
        print(f"{div:.1f}")
        