A, B = map(float, input().split())

if A%B == 0 or B%A == 0:
    print("São Multiplos")
else:
    print("Não são Multiplos")