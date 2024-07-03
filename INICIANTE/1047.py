hora_inicio, minuto_inicio, hora_final, minuto_final = map(int, input().strip().split())

uma_hora = 60
um_dia = 24

# Convertendo os horários de início e fim para minutos desde a meia-noite
total_minutos_inicio = hora_inicio * uma_hora + minuto_inicio
total_minutos_final = hora_final * uma_hora + minuto_final

# Calculando a diferença em minutos
if total_minutos_inicio <= total_minutos_final:
    duracao_em_minutos = (total_minutos_final + (um_dia * uma_hora)) - total_minutos_inicio
    if duracao_em_minutos // um_dia >= um_dia * uma_hora:
        duracao_em_minutos = total_minutos_final - total_minutos_inicio
else:
    duracao_em_minutos = (um_dia * uma_hora) - (total_minutos_inicio - total_minutos_final)

# Convertendo a diferença de minutos para horas e minutos
duracao_horas = duracao_em_minutos // uma_hora
duracao_minutos = duracao_em_minutos % uma_hora

# Saída formatada
print(f"O JOGO DUROU {duracao_horas} HORA(S) E {duracao_minutos} MINUTO(S)")
