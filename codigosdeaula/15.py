valor = float(input())

valor = int(valor * 100)

nota100 = valor//10000
valor %= 10000
nota50 = valor//5000
valor %= 5000
nota20 = valor//2000
valor %= 2000
nota10 = valor//1000
valor %= 1000
nota5 = valor//500
valor %= 500
nota2 = valor//200
valor %= 200

moeda100 = valor//100
valor %= 100
moeda50 = valor//50
valor %= 50
moeda25 = valor//25
valor %= 25
moeda10 = valor//10
valor %= 10
moeda5 = valor//5
valor %= 5
moeda1 = valor

print("NOTAS:")
print(f"{nota100} nota(s) de R$ 100.00")
print(f"{nota50} nota(s) de R$ 50.00")
print(f"{nota20} nota(s) de R$ 20.00")
print(f"{nota10} nota(s) de R$ 10.00")
print(f"{nota5} nota(s) de R$ 5.00")
print(f"{nota2} nota(s) de R$ 2.00")

print("MOEDAS:")
print(f"{moeda100} moeda(s) de R$ 1.00")
print(f"{moeda50} moeda(s) de R$ 0.50")
print(f"{moeda25} moeda(s) de R$ 0.25")
print(f"{moeda10} moeda(s) de R$ 0.10")
print(f"{moeda5} moeda(s) de R$ 0.05")
print(f"{moeda1} moeda(s) de R$ 0.01")