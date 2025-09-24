lados = input().split()

A, B, C = sorted(map(float, lados), reverse=True)

if A >= (B + C):
    print("NAO FORMA TRIANGULO")
else:
    if (A * A) == ((B * B) + (C * C)):
        print("TRIANGULO RETANGULO")
    elif (A * A) > ((B * B) + (C * C)):
        print("TRIANGULO OBTUSANGULO")
    elif (A * A) < ((B * B) + (C * C)):
        print("TRIANGULO ACUTANGULO")

lados = [A, B, C]

if lados.count(A) == 2 or lados.count(B) == 2:
    print("TRIANGULO ISOSCELES")
if lados.count(A) == 3:
    print("TRIANGULO EQUILATERO")