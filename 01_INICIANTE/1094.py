n = int(input())

tipo_c = 0
tipo_r = 0
tipo_s = 0

for i in range(n):
    quantia, tipo = input().split()
    quantia = int(quantia)

    if tipo.upper() == "C":
        tipo_c += quantia
    elif tipo.upper() == "R":
        tipo_r += quantia
    elif tipo.upper() == "S":
        tipo_s += quantia

total_cobaias = tipo_s + tipo_c + tipo_r

print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {tipo_c}")
print(f"Total de ratos: {tipo_r}")
print(f"Total de sapos: {tipo_s}")
print(f"Percentual de coelhos: {(tipo_c/total_cobaias)*100:.2f} %")
print(f"Percentual de ratos: {(tipo_r/total_cobaias)*100:.2f} %")
print(f"Percentual de sapos: {(tipo_s/total_cobaias)*100:.2f} %")
