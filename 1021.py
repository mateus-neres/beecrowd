x = float(input())

cedulas = [100.00,50.00,20.00,10.00,5.00,2.00]
moedas = [1.00,0.50,0.25,0.10,0.05,0.01]

print("NOTAS:")

for cedeula in cedulas:
    decomposicao = x // cedeula
    x = round(x % cedeula, 2)
    print(f"{decomposicao:.0f} nota(s) de R$ {cedeula:.2f}")

print("MOEDAS:")

for moeda in moedas:
    decomposicao = x // moeda
    x = round(x % moeda,2)
    print(f"{decomposicao:.0f} moeda(s) de R$ {moeda:.2f}")
