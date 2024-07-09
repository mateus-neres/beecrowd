a = input()
b = input()
c = input()

if a.lower() ==  'vertebrado':

    if b.lower() == 'ave':

        if c.lower() == 'carnivoro':
            print('aguia')

        elif c.lower() == 'onivoro':
            print('pomba')

    elif b.lower() == 'mamifero':

        if c.lower() == 'onivoro':
            print('homem')

        elif c.lower() == 'herbivoro':
            print('vaca')

elif a.lower() == 'invertebrado':
    
    if b.lower() == 'inseto':

        if c.lower() == 'hematofago':
            print('pulga')

        elif c.lower() == 'herbivoro':
            print('lagarta')

    elif b.lower() == 'anelideo':

        if c.lower() == 'hematofago':
            print('sanguessuga')

        elif c.lower() == 'onivoro':
            print('minhoca')
