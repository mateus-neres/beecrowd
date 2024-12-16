def simplificar(nume, deno):

    a, b = nume, deno
    while b != 0:
        a, b = b, a % b
    mdc = a

    return nume // mdc, deno // mdc

entrada = int(input())

lista = []

for _ in range(entrada):

    numerador_1, divisor, denominador_1, operador, numerador_2, divisor, denominador_2 = input().split(" ")
    numerador_1, denominador_1 = int(numerador_1), int(denominador_1)
    numerador_2, denominador_2 = int(numerador_2), int(denominador_2)

    if operador == "*":
        numerador = numerador_1 * numerador_2
        denominador = denominador_1 * denominador_2

    elif operador == "/":
        numerador = numerador_1 * denominador_2
        denominador = denominador_1 * numerador_2

    elif operador == "+":
        numerador = numerador_1 * denominador_2 + numerador_2 * denominador_1
        denominador = denominador_1 * denominador_2

    elif operador == "-":
        numerador = numerador_1 * denominador_2 - numerador_2 * denominador_1
        denominador = denominador_1 * denominador_2

    nume_simp, deno_simp = simplificar(numerador, denominador)
    lista.append(f"{numerador}/{denominador} = {nume_simp}/{deno_simp}")

for resultado in lista:
    print(resultado)
