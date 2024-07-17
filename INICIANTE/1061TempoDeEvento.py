texto1, dia_inicio = map(str, input().strip().split())
dia_inicio = int(dia_inicio)
hi, mi, si = map(int, input().strip().split(":"))

texto2, dia_fim = map(str, input().strip().split())
dia_fim = int(dia_fim)
hf, mf, sf = map(int, input().strip().split(":"))

tempo_inicio_segundos = (dia_inicio * 86400) + (hi * 3600) + (mi * 60) + si

tempo_fin_segundos = (dia_fim * 86400) + (hf * 3600) + (mf * 60) + sf

diferenca = tempo_fin_segundos - tempo_inicio_segundos

dias = diferenca // 86400
horas = (diferenca % 86400) // 3600
minutos = ((diferenca % 86400) % 3600) // 60
segundos = ((diferenca % 86400) % 3600) % 60

print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')
