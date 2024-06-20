CARRO_X = 60
CARRO_Y = 90
HORA = 60

if CARRO_X > CARRO_Y:
    diferenca = (CARRO_X - CARRO_Y) / HORA
else:
    diferenca = (CARRO_Y - CARRO_X) / HORA

km = int(input())

tempo = km / diferenca

print(f"{tempo:.0f} minutos")
