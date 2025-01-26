S = 0.0
numerador = 1
denominador = 1

while numerador <= 39:
    S += numerador / denominador

    numerador += 2
    denominador *= 2

print(f"{S:.2f}")
