X = float(input())

N = [X]

for i in range(1, 100):
    N.append(N[i-1] / 2)

for i in range(len(N)):
    print(f"N[{i}] = {N[i]:.4f}")
    