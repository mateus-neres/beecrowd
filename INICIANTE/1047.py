hora_inicio, minuto_inicio, hora_fim, minuto_fim = map(int, input().strip().split())
dia = 24
hora = 60

if hora_inicio >= hora_fim and minuto_inicio >= minuto_fim:

    hora_fim = hora_fim + dia
    minuto_fim = minuto_fim + hora
    diferenca_hora = hora_fim - hora_inicio
    diferenca_minuto =  minuto_fim - minuto_inicio

    if diferenca_hora>= dia:
        diferenca_minuto = 0
        print(f"O JOGO DUROU {diferenca_hora} HORA(S) E {diferenca_minuto} MINUTO(S)")

    elif diferenca_hora <= 1:
        diferenca_hora = 0
        diferenca_minuto = hora - diferenca_minuto
        print(f"O JOGO DUROU {diferenca_hora} HORA(S) E {diferenca_minuto} MINUTO(S)")

else:
    diferenca_hora = hora_fim - hora_inicio
    diferenca_minuto =  minuto_fim - minuto_inicio
    diferenca_minuto =  minuto_fim - minuto_inicio

    if minuto_inicio >= minuto_fim:
        minuto_fim = minuto_fim + hora
        diferenca_minuto =  minuto_fim - minuto_inicio
        if diferenca_hora>= dia:
            diferenca_minuto = 0
            print(f"O JOGO DUROU {diferenca_hora} HORA(S) E {diferenca_minuto} MINUTO(S)")

        elif diferenca_hora <= 1:
            diferenca_hora = 0
            diferenca_minuto = hora - diferenca_minuto
            print(f"O JOGO DUROU {diferenca_hora} HORA(S) E {diferenca_minuto} MINUTO(S)")
