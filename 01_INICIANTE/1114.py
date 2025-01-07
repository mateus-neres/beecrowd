SENHA = 2002
control = True
while control:
    entrada = int(input())
    if entrada == SENHA:
        print("Acesso Permitido")
        control = False
    else:
        print("Senha Invalida")
        