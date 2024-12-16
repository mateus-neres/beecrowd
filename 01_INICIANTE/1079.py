entrada = int(input())

media_ponderada = []

for i in range(1, entrada + 1):
    v1, v2, v3 = map(float, input().split(" "))
    media = ((v1 * 2) + (v2 * 3) + (v3 * 5)) / (10)
    media_ponderada.append(media)

for indice in range(len(media_ponderada)):
    print(f'{media_ponderada[indice]:.1f}')
