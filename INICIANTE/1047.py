hora_inicio, minuto_inicio, hora_fim, minuto_fim = map(int, input().strip().split())

# Calcula o tempo total em minutos
inicio_total_minutos = hora_inicio * 60 + minuto_inicio
fim_total_minutos = hora_fim * 60 + minuto_fim


# Calcula a duração em minutos, considerando que pode passar de um dia para o outro
if fim_total_minutos >= inicio_total_minutos:
    duracao_total_minutos = fim_total_minutos - inicio_total_minutos
else:
    duracao_total_minutos = (24 * 60 - inicio_total_minutos) + fim_total_minutos

# Se a duração for 0 minutos, ajusta para 1 minuto
if duracao_total_minutos == 0:
    duracao_total_minutos = 1

# Converte a duração total de minutos em horas e minutos
duracao_horas = duracao_total_minutos // 60
duracao_minutos = duracao_total_minutos % 60

print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")