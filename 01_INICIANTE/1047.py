hora_inicio, minuto_inicio, hora_final, minuto_final = map(int, input().strip().split())

minutos_inicio = (hora_inicio * 60) + minuto_inicio
minutos_final = (hora_final * 60) + minuto_final

if minutos_inicio > minutos_final:

    duracao = (1440 - minutos_inicio) + minutos_final
else:

    duracao = minutos_final - minutos_inicio

hora = duracao // 60
minuto = duracao % 60

print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")
