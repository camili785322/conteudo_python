#Faça um programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

numero = int(input("Digite um número de 1 a 7: "))

if numero == 1:
    print("Correspondente a Domingo ")

elif numero == 2:
    print("Correspondente a Segunda ")

elif numero == 3:
    print("Correspondente a Terça ")

elif numero == 4:
    print("Correspondente a Quarta ")

elif numero == 5:
    print("Correspondente a Quinta  ")

elif numero == 6:
    print("Correspondente a Sexta  ")

elif numero == 7:
    print("Correspondente a Sabado ")

else:
    print("Digite apenas números de 1 a 7")