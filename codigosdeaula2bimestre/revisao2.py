numerosecreto = 5

tentativa1 = int(input("Adivinhe o número entre 1 e 10: "))

if tentativa1 < 1:
    print("Palpite Inválido")
if tentativa1 > 10:
    print("Palpite Inválido")
if tentativa1 == numerosecreto:
    print("Acertou")

if tentativa1 < numerosecreto:
    if tentativa1 >= 1:
        if tentativa1 <= 10:
            print("Muito Baixo")
        
if tentativa1 > numerosecreto:
    if tentativa1 >= 1:
        if tentativa1 <= 10:
            print("Muito Alto")

if tentativa1 != numerosecreto:
    tentativa2 = int(input("Adivinhe o número entre 1 e 10: "))

    if tentativa2 < 1:
        print("Palpite Inválido")
    if tentativa2 > 10:
        print("Palpite Inválido")
    if tentativa2 == numerosecreto:
        print("Acertou")

    if tentativa2 < numerosecreto:
        if tentativa2 >= 1:
            if tentativa2 <= 10:
                print("Muito Baixo")
        
    if tentativa2 > numerosecreto:
        if tentativa2 >= 1:
            if tentativa2 <= 10:
                print("Muito Alto")

if tentativa2 != numerosecreto:
    tentativa3 = int(input("Adivinhe o número entre 1 e 10: "))

    if tentativa3 < 1:
        print("Palpite Inválido")
    if tentativa3 > 10:
        print("Palpite Inválido")
    if tentativa3 == numerosecreto:
        print("Acertou")

    if tentativa3 < numerosecreto:
        if tentativa3 >= 1:
            if tentativa3 <= 10:
                print("Muito Baixo")
        
    if tentativa3 > numerosecreto:
        if tentativa3 >= 1:
            if tentativa3 <= 10:
                print("Muito Alto")
    
        if tentativa3 != numerosecreto:
            print(f"Fim de jogo. O certo seria o número {numerosecreto}.")

