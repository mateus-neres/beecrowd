n = int(input())

while n != 0:

   lista = []
   for i in range(1, n+1):
      lista.append(i)
   
   print(" ".join(map(str, lista)))

   n = int(input())
   