import math
a, b, c = map(float, input().strip().split())

delta = (b**2) - (4*a*c)

if delta > 0:
	if a == 0:
		print("Impossivel calcular")
	else:
		r1 = (-b + math.sqrt(delta)) / (2 * a)
		r2 = (-b - math.sqrt(delta)) / (2 * a)
		print(f"R1 = {r1:.5f}")
		print(f"R2 = {r2:.5f}")
else:
	print("Impossivel calcular")
