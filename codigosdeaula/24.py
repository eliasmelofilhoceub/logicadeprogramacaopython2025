filo = input()
classe = input()
tipo = input()

if filo == 'vertebrado':
    if classe == 'ave':
        if tipo == 'carnivoro':
            print('aguia')
        elif tipo == 'onivoro':
            print('pomba')
    elif classe == 'mamifero':
        if tipo == 'onivoro':
            print('homem')
        elif tipo == 'herbivoro':
            print('vaca')

if filo == 'invertebrado':
    if classe == 'inseto':
        if tipo == 'hematofago':
            print('pulga')
        elif tipo == 'herbivoro':
            print('lagarta')
    elif classe == 'anetidio':
        if tipo == 'hematofago':
            print('sanguessuga')
        elif tipo == 'onivoro':
            print('minhoca')