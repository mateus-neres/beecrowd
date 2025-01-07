hora_inicio, minuto_inicio, hora_fim, minuto_fim = map(int, input().split())

temp_inicio = (hora_inicio * 60) + minuto_inicio
temp_fim = (hora_fim * 60) + minuto_fim

if temp_inicio < temp_fim:
    tempo = temp_fim - temp_inicio
else:
    tempo = (24 * 60 - temp_inicio) + temp_fim

horas = tempo // 60
minutos = tempo % 60

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")
