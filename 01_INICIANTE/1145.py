x, y = map(int, input().split())
incremento = 1
for i in range(1, y+1):
	
	lista = []
	control = 0
	
	while control < x:
		lista.append(incremento)
		incremento += 1
		control += 1
		if incremento == y + 1:
			break
		
		
	print(" ".join(map(str, lista)))
	if incremento == y +1:
		break
		