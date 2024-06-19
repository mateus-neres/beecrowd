codigo1, quatidade1, valor1 = input().split()
codigo1 = int(codigo1)
quatidade1 = int(quatidade1)
valor1 = float(valor1)

codigo2, quatidade2, valor2 = input().split()
codigo2 = int(codigo2)
quatidade2 = int(quatidade2)
valor2 = float(valor2)

valor_pagar = (quatidade1 * valor1) + (quatidade2 * valor2)

print(f"VALOR A PAGAR: R$ {valor_pagar:.2f}")
