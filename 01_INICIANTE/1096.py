i = 1
j = 7
cont = 0

while i <= 9:
	cont += 1
	print(f"I={i} J={j}")
	j -= 1
	if cont == 3:
		cont = 0
		i +=2
		j = 7