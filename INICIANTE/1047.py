hora_inicio, minuto_inicio, hora_final, minuto_final = map(int, input().strip().split())

uma_hora = 60
um_dia = 24



if hora_inicio <= hora_final:

    total_minutos_inicio = (hora_inicio + um_dia) * uma_hora + minuto_inicio
    total_minutos_final = hora_final * uma_hora + minuto_final
    horas = (total_minutos_inicio // uma_hora) - (total_minutos_final // uma_hora)
    minutos = (total_minutos_final % uma_hora) - (total_minutos_inicio % uma_hora) 
    print(horas)
    print(minutos)  
else:
    total_minutos_inicio = hora_inicio * uma_hora + minuto_inicio
    total_minutos_final = hora_final * uma_hora + minuto_final
    horas = (total_minutos_final // uma_hora) - (total_minutos_inicio // uma_hora)
    minutos = (total_minutos_final % uma_hora) - (total_minutos_inicio % uma_hora)
    print(horas)
    print(minutos)