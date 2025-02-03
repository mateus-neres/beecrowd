T = int(input())

fib = [0,1]
for i in range(2, 61):
    fib.append(fib[i - 1] + fib[i - 2])

for i in range(T):
    N = int(input())

    print(f'Fib({N}) = {fib[N]}')
