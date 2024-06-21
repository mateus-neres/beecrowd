x = int(input())

anos = x // 365
resto = x % 365

meses = resto // 30
resto = resto % 30

dias = resto

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")
