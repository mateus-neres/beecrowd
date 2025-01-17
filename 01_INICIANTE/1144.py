n = int(input())

for i in range(1, n+1):

    control = 0
    
    while True:
        
        print(f"{i} {(i**2)+control} {(i ** 3) + control}")
        control += 1
        if control == 2:
            break
