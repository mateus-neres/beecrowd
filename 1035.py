a = int(input())
b = int(input())
c = int(input())
d = int(input())

if b > c and d > a:
	if (c + d ) > (a + b):
		if c >= 0 and d >= 0:
			if a % 2 == 0:
				print("Valores aceitos")
			else:
				print("Valores nao aceitos")	
		else:
			print("Valores nao aceitos")
	else:
		print("Valores nao aceitos")
else:
	print("Valores nao aceitos")
