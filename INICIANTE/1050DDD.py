codigo = int(input())

lista_codigos = ['61:Brasilia','71:Salvador','11:Sao Paulo','21:Rio de Janeiro','32:Juiz de Fora','19:Campinas','27:Vitoria','31:Belo Horizonte']

cidade_encontrada = False

for item in lista_codigos:
    ddd, cidade = item.split(':', 1)
    if codigo == int(ddd):
        print(cidade)
        cidade_encontrada = True

if not cidade_encontrada:
    print('DDD nao cadastrado')
