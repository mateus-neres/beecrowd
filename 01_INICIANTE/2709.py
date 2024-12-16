def eh_primo(numero):
    """Função para verificar se um número é primo."""
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


def processar_jogo():
    import sys
    entrada = sys.stdin.read()
    linhas = entrada.splitlines()

    i = 0
    while i < len(linhas):
        # Lê a quantidade de moedas
        M = int(linhas[i])
        i += 1

        # Lê os valores das moedas
        valores = []
        for _ in range(M):
            valores.append(int(linhas[i]))
            i += 1

        # Lê o salto
        N = int(linhas[i])
        i += 1

        # Calcula a soma dos valores com base no salto
        soma = 0
        for j in range(M - 1, -1, -N):
            soma += valores[j]

        # Verifica se a soma é um número primo
        if eh_primo(soma):
            print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
        else:
            print("Bad boy! I’ll hit you.")


# Executa o jogo
processar_jogo()