pares = 0
impares = 0
positivos =0
negativos = 0
controle = 0
while controle < 5:
    entrada = int(input())
    if entrada % 2 == 0:
        pares += 1
    if entrada % 2 != 0:
        impares += 1
    if entrada < 0:
        negativos += 1
    if entrada > 0:
        positivos += 1
    controle+=1

print(f'{pares} valor(es) par(es)')
print(f'{impares} valor(es) impar(es)')
print(f'{positivos} valor(es) positivo(s)')
print(f'{negativos} valor(es) negativo(s)')
