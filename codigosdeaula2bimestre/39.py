linha = int(input())
operacao = input()

matriz = []

for i in range(12):

    linhaMatriz = []

    for j in range(12):
    
        linhaMatriz.append(float(input()))
    
    matriz.append(linhaMatriz)

resultado = sum(matriz[linha])

if operacao == "M":
    resultado = resultado / 12

print(resultado)