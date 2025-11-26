numeros = list(map(int, input().split()))

auxNumeros = list(numeros)

numeros.sort()

for n in numeros:
    print(n)

print()

for n in auxNumeros:
    print(n)