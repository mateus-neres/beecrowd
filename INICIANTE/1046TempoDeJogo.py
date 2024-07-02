a, b = map(int, input().strip().split())

horas_dia = 24

if a >= b:
    b = horas_dia + b
    tempo_jogo = b - a
    print(f"O JOGO DUROU {tempo_jogo} HORA(S)")
else:
    tempo_jogo = b - a
    print(f"O JOGO DUROU {tempo_jogo} HORA(S)")
