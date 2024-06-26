codigo, quantidade = map(int, input().strip().split())

lista = [
    [1,'Cachorro Quente', 4.00],
    [2, 'X-Salada',4.50],
    [3,'XBacon',5.00],
    [4,'Torrada Simples',2.00],
    [5,'Refrigerante',1.50]
]
total_a_pagar = 0
for indice in range(len(lista)):
    if lista[indice][0] == codigo:
        total_a_pagar += lista[indice][2] * quantidade
print(f'Total: R$ {total_a_pagar:.2f}')
