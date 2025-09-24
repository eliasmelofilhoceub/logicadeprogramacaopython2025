preco = 20.0

idade = int(input("Digite sua idade: "))
estudante = input("É estudante s/n: ")

if idade < 0 or idade > 120:
    print("Idade Inválida")
else:
    if idade < 12:
        precofinal = preco / 2
        indicacao = "meia entrada criança"
    else:
        if idade >= 60:
            precofinal = preco / 2
            indicacao = "meia entrada idoso"
        else:
            if estudante == "s":
                precofinal = preco / 2
                indicacao = "meia entrada estudante"
            else:
                precofinal = preco
                indicacao = "valor integral"

print(f"Valor do Ingresso: R$ {precofinal} ({indicacao})")                