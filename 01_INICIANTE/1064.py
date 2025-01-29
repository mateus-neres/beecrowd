contador = 0
total = 0

for i in range(6):
    
    entrada = float(input())
    if entrada > 0:
        contador += 1
        total += entrada
 
media = total / contador       
    
print(f'{contador} valores positivos')
print(f'{media:.1f}')
