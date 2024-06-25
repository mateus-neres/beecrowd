import math
a = float(input())
b = float(input())
c = float(input())

if a != 0:
	r1 = (-b + math.sqrt((b**2) - (4 * a * c))) / (2 * a)
	if r1 < 0:
		print("Impossivel calcular")
	else:
		r2 = (-b - math.sqrt((b**2) - (4 * a * c))) / (2 * a)
		print(f"R1 = {r1:.5f}")
		print(f"R2 = {r2:.5f}")
else:
	print("Impossivel calcular")
