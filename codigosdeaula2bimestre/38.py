N = int(input())

vetor = input()

vetor = vetor.split()

vetor = map(int, vetor)

vetor = list(vetor)

menor = min(vetor)

posicao = vetor.index(menor)

print(f'Menor Valor:', menor)
print(f'Posicao:', posicao)