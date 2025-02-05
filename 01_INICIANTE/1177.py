T = int(input())
N = []
control = 0
for i in range(1000):

    N.append(control)

    if control < T-1:
        control += 1
    else:
        control = 0
        

for _ in range(len(N)):
    print(f"N[{_}] = {N[_]}")
