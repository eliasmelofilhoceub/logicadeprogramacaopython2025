M, N = map(int, input().split(" "))

while M > 0 and N > 0:

    if N < M:
        aux = N
        N = M
        M = aux
    
    resultado = []
    strResultado = ""

    for i in range(M, N + 1, 1):
        resultado.append(i)

        strResultado += str(i) + " "
    
    print(f"{strResultado}Sum={sum(resultado)}")

    M, N = map(int, input().split(" "))
