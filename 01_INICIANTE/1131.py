vitoria_gremio = 0
vitoria_inter = 0
empates = 0
grenais = 0

while True:
    inter, gremio = map(int, input().split())

    if inter > gremio:
        vitoria_inter += 1
    elif gremio > inter:
        vitoria_gremio += 1
    else:
        empates += 1
    grenais += 1

    while True:
        print("Novo grenal (1-sim 2-nao)")
        n = int(input())
        if n == 1 or n == 2:
            break

    if n == 2:
        break

print(f"{grenais} grenais")
print(f"Inter:{vitoria_inter}")
print(f"Gremio:{vitoria_gremio}")
print(f"Empates:{empates}")

if vitoria_inter > vitoria_gremio:
    print("Inter venceu mais")
elif vitoria_gremio > vitoria_inter:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")
