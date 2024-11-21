a, b = map(int, input().strip().split())

if b % a == 0 or a % b == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
