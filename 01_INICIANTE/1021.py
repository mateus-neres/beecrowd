x = float(input())

cedulas = [100.00,50.00,20.00,10.00,5.00,2.00]
moedas = [1.00,0.50,0.25,0.10,0.05,0.01]

centavos = int(x * 100)

print("NOTAS:")

for cedula in cedulas:
    valor_centavos = int(cedula * 100)
    decomposicao = centavos // valor_centavos
    centavos = centavos % valor_centavos
    print(f"{decomposicao:.0f} nota(s) de R$ {cedula:.2f}")

print("MOEDAS:")

for moeda in moedas:
    valor_centavos = int(moeda * 100)
    decomposicao = centavos // valor_centavos
    centavos = centavos % valor_centavos
    print(f"{decomposicao:.0f} moeda(s) de R$ {moeda:.2f}")
