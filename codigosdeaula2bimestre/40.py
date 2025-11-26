def criaMatriz():

    matriz = [[0 for i in range(12)] for j in range(12)]
    return matriz

def preencherMatriz(matriz):

    for i in range(12):
        for j in range(12):

            matriz[i][j] = float(input())

def soma(matriz, coluna):
    total = 0
    for i in range(12):
        total += matriz[i][coluna]
    return total

def media(matriz, coluna):
    return soma(matriz, coluna) / 12

C = int(input())

T = input()

M = criaMatriz()
preencherMatriz(M)

if T == 'S':
    print(f"{soma(M, C):.1f}")

elif T == 'M':
    print(f"{media(M, C):.1f}")