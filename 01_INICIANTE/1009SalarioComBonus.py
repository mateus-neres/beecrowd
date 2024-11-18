nome = input()
salario = float(input())
vendas = float(input())

comissao = salario + (0.15 * vendas)

print(f"TOTAL = R$ {comissao:.2f}")
