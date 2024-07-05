hora_inicio, minuto_inicio, hora_final, minuto_final = map(int, input().strip().split())

if hora_inicio >= hora_final:
    horas_para_minuto_inicio = ((hora_inicio + 24) * 60) + minuto_inicio
    horas_para_minuto_final = (hora_final * 60) + minuto_final
    hora =  (horas_para_minuto_inicio - horas_para_minuto_final) // 60
    minuto = (horas_para_minuto_inicio % horas_para_minuto_final) // 60
else:
    horas_para_minuto_inicio = (hora_inicio * 60) + minuto_inicio
    horas_para_minuto_final = (hora_final * 60) + minuto_final
    hora =  (horas_para_minuto_final - horas_para_minuto_inicio) // 60
    minuto = (horas_para_minuto_final % horas_para_minuto_inicio)

print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")
