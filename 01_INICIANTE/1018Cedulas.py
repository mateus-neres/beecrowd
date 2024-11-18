x = int(input())

cedulas = [100,50,20,10,5,2,1]

print(x)

for cedeula in cedulas:
    decomposicao = x // cedeula
    x = x % cedeula
    print(f"{decomposicao:.0f} nota(s) de R$ {cedeula},00")
