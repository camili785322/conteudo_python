#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
#sabendo que a decisão é sempre pelo mais barato

preco1 = float(input("Digite o preço do produto 1: "))
preco2 = float(input("Digite o preço do produto 2: "))
preco3 = float(input("Digite o preço do produto 3: "))

if preco1 <= preco2 and preco3:
    print("O produto com menor preço é: ", preco1)
elif preco2 <= preco1 and preco2 <= preco3:
    print("O produto com o menor preço é: ", preco2)
else:
    print("o produto com o menor preço é: ", preco3)