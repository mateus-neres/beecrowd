VP = []
VI = []
for i in range(15):
    X = int(input())

    if X % 2 == 0:
        VP.append(X)
        if len(VP) == 5:
            for i in range(len(VP)):
                print(f'par[{i}] = {VP[i]}')
            VP = []    
    elif X % 2 != 0:
        VI.append(X)
        if len(VI) == 5:
            for i in range(len(VI)):
                print(f'impar[{i}] = {VI[i]}')
            VI = []    


for i in range(len(VI)):
    print(f'impar[{i}] = {VI[i]}')

for i in range(len(VP)):
    print(f'par[{i}] = {VP[i]}')
