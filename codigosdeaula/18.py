item, qtdItem = map(float, input().split(' '))

if (item == 1):
    preco = 4.00*qtdItem
elif (item == 2):
    preco = 4.50*qtdItem
elif (item == 3):
    preco = 5.00*qtdItem
elif (item == 4):
    preco = 2.00*qtdItem
elif (item == 5):
    preco = 1.50*qtdItem

print(f"Total: R$ {preco:.2f}")