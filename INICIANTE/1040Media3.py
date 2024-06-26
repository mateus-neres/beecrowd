n1, n2, n3, n4 = map(float, input().strip().split())

peso_n1 = 2
peso_n2 = 3
peso_n3 = 4
peso_n4 = 1

soma_peso = peso_n1 + peso_n2 + peso_n3 + peso_n4

media = ((peso_n1 * n1) + (peso_n2 * n2) + (peso_n3 * n3) + (peso_n4 * n4)) / soma_peso
print(f'Media: {media:.1f}')

if media >= 7:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    n5 = float(input())
    print(f'Nota do exame: {n5}')
    media_final = (media + n5) / 2
    if media_final >= 5:
        print('Aluno aprovado.')
        print(f'Media final: {media_final:.1f}')
    else:
        print('Aluno reprovado.')
        print(f'Media final: {media_final:.1f}')
