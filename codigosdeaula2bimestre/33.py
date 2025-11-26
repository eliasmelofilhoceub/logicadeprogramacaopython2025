while (nota1 := float(input())) < 0 or nota1 > 10: print('Nota Invalida')
    
while (nota2 := float(input())) < 0 or nota2 > 10: print('Nota Invalida')

print(f'media = {(nota1 + nota2)/2.0}')