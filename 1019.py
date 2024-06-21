x = int(input())

horas = x // 3600
resto = x % 3600

minutos = resto // 60
resto = resto % 60

segundos = resto

print(f"{horas}:{minutos}:{segundos}")