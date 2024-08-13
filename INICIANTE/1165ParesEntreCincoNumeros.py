contador = 0
controle = 0
while controle < 5:
    entrada = int(input())
    if entrada % 2 == 0:
        contador += 1
    controle += 1
print(f'{contador} valores pares')    
    